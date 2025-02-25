# Ansible Callback Plugins Directory

## 📌 What is the `callback_plugins/` Directory?
The `callback_plugins/` directory in an Ansible project is used to **store custom callback plugins** that modify how playbook output is handled and logged.

## 📦 Why Use the `callback_plugins/` Directory?
- 🛠 **Enhances logging and event handling** during playbook execution.
- 🔄 **Runs additional scripts or hooks** automatically.
- 🚀 **Customizes output formatting and logging behavior** beyond Ansible defaults.

## 📄 How to Structure the `callback_plugins/` Directory
A typical `callback_plugins/` directory contains:
```
callback_plugins/
├── setup_script.py  # Runs setup.sh before playbooks and logs events
├── custom_logger.py  # Example: Logs playbook execution to external service
```

## 🔍 Creating a Custom Callback Plugin
Callback plugins extend Ansible's logging and event handling features.

### 🔹 Example: `callback_plugins/setup_script.py`
```python
from ansible.plugins.callback import CallbackBase
import subprocess
import os
import datetime
import traceback

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'setup_script'

    def __init__(self):
        super(CallbackModule, self).__init__()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.log_dir = "log"
        self.log_file = os.path.join(self.log_dir, f"ansible_run_{timestamp}.log")
        self.detailed_errors = os.getenv("ANSIBLE_DETAILED_ERRORS", "false").lower() in ["true", "1", "yes"]
        os.makedirs(self.log_dir, exist_ok=True)

    def v2_playbook_on_start(self, playbook):
        self._display.banner("Running setup script before playbook execution...")
        try:
            subprocess.run(["./setup.sh"], check=True)
        except subprocess.CalledProcessError as e:
            self._display.error(f"Setup script failed: {e}")
```

## 🚀 Configuring Ansible to Use Custom Callback Plugins
Modify `ansible.cfg` to enable the plugin:
```ini
[defaults]
callback_plugins = ./callback_plugins
callbacks_enabled = default, setup_script
```

## 🏆 Best Practices
- **Ensure callback plugins have unique names** to avoid conflicts.
- **Use callback plugins to log events** or modify output formats.
- **Keep logs structured and stored in a dedicated `log/` directory**.
- **Test new callback plugins separately** before integrating them into production playbooks.

The `callback_plugins/` directory enhances automation by enabling custom event handling, logging, and pre-execution hooks tailored to your environment.
