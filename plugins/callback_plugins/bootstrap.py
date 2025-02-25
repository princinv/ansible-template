from ansible.plugins.callback import CallbackBase
import subprocess
import os
import datetime
# export ANSIBLE_DETAILED_ERRORS=true

class CallbackModule(CallbackBase):
    """
    Custom callback plugin to run setup.sh before playbook execution and log events.
    """
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'setup_script'

    def __init__(self):
        super(CallbackModule, self).__init__()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.log_dir = "log"
        self.log_file = os.path.join(self.log_dir, f"ansible_run_{timestamp}.log")
        os.makedirs(self.log_dir, exist_ok=True)
        
        with open(self.log_file, "a") as log:
            log.write("\n=== New Ansible Run: {} ===\n".format(timestamp))

    def v2_playbook_on_start(self, playbook):
        self._display.banner("Running setup script before playbook execution...")
        with open(self.log_file, "a") as log:
            log.write("Running setup script before playbook execution...\n")
        
        try:
            subprocess.run(["./setup.sh"], check=True)
        except subprocess.CalledProcessError as e:
            with open(self.log_file, "a") as log:
                log.write(f"Setup script failed: {e}\n")
            self._display.error(f"Setup script failed: {e}")

    def v2_runner_on_ok(self, result):
        """Logs successful tasks."""
        with open(self.log_file, "a") as log:
            log.write(f"TASK OK: {result._task.get_name()}\n")

    def v2_runner_on_failed(self, result, ignore_errors=False):
        """Logs failed tasks."""
        with open(self.log_file, "a") as log:
            log.write(f"TASK FAILED: {result._task.get_name()}\n")

    def v2_runner_on_skipped(self, result):
        """Logs skipped tasks."""
        with open(self.log_file, "a") as log:
            log.write(f"TASK SKIPPED: {result._task.get_name()}\n")

    def v2_playbook_on_stats(self, stats):
        """Logs playbook completion status."""
        with open(self.log_file, "a") as log:
            log.write("=== Playbook Execution Complete ===\n")
