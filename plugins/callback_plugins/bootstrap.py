# plugins/callback_plugins/bootstrap.py

# ==========================================
# ANSIBLE CALLBACK: bootstrap
# ==========================================
# Purpose:
#   Run a repo-local bootstrap script *once* before the playbook starts.
#   Logs all callback events to log/ansible_run_<timestamp>.log
#
# Config:
#   - Set in ansible.cfg:
#       [defaults]
#       callbacks_enabled = profile_tasks,bootstrap
#   - Optional env:
#       BOOTSTRAP_PATH (default: ./bootstrap.sh)
#
# Behavior:
#   - If the bootstrap script is missing: log a warning and continue.
#   - If present and exits non-zero: print error and continue (does not crash Ansible).
#     Flip `fail_on_error` below to make failures fatal if you prefer.
# 

from ansible.plugins.callback import CallbackBase
import subprocess
import os
import datetime

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'bootstrap'

    def __init__(self):
        super(CallbackModule, self).__init__()
        ts = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.log_dir = "log"
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_file = os.path.join(self.log_dir, f"ansible_run_{ts}.log")
        self.fail_on_error = True  # set True to make bootstrap failure abort the run

        with open(self.log_file, "a") as log:
            log.write(f"\n=== New Ansible Run: {ts} ===\n")

    def _run_bootstrap(self):
        script_path = os.environ.get("BOOTSTRAP_PATH", "./bootstrap.sh")
        script_abs = os.path.abspath(script_path)

        with open(self.log_file, "a") as log:
            log.write(f"Bootstrap path: {script_abs}\n")

        if not os.path.isfile(script_abs):
            self._display.warning(f"bootstrap: '{script_abs}' not found; skipping.")
            with open(self.log_file, "a") as log:
                log.write("bootstrap: script missing; skipped.\n")
            return True

        # Stream output into the log file
        with open(self.log_file, "a") as log:
            log.write("Running bootstrap script...\n")
            try:
                proc = subprocess.run(
                    ["bash", script_abs],
                    check=False,
                    stdout=log,
                    stderr=log,
                )
            except Exception as e:
                self._display.error(f"bootstrap: exception: {e}")
                log.write(f"bootstrap: exception: {e}\n")
                return not self.fail_on_error

        if proc.returncode != 0:
            msg = f"bootstrap: exited with {proc.returncode}"
            if self.fail_on_error:
                self._display.error(msg)
                return False
            else:
                self._display.warning(msg + " (continuing)")
                with open(self.log_file, "a") as log:
                    log.write(msg + " (continuing)\n")
        else:
            with open(self.log_file, "a") as log:
                log.write("bootstrap: completed successfully.\n")
        return True

    def v2_playbook_on_start(self, playbook):
        self._display.banner("Running bootstrap script before playbook execution...")
        ok = self._run_bootstrap()
        if not ok:
            # If fail_on_error=True and bootstrap failed:
            raise Exception("bootstrap callback: configured to fail on error")

    def v2_runner_on_ok(self, result):
        with open(self.log_file, "a") as log:
            log.write(f"TASK OK: {result._task.get_name()}\n")

    def v2_runner_on_failed(self, result, ignore_errors=False):
        with open(self.log_file, "a") as log:
            log.write(f"TASK FAILED: {result._task.get_name()}\n")

    def v2_runner_on_skipped(self, result):
        with open(self.log_file, "a") as log:
            log.write(f"TASK SKIPPED: {result._task.get_name()}\n")

    def v2_playbook_on_stats(self, stats):
        with open(self.log_file, "a") as log:
            log.write("=== Playbook Execution Complete ===\n")
