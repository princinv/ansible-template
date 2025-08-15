# Ansible Module Utils Directory
module_utils/README.md

## What is the `module_utils/` Directory?

The `module_utils/` directory in an Ansible project or role is used to **store shared Python utility functions** that can be reused across multiple custom modules.

## Why Use the `module_utils/` Directory?

* **Encapsulates reusable code** to avoid duplication across custom modules.
* **Improves maintainability** by centralizing logic in a single place.
* **Ensures consistency** when writing multiple related Ansible modules.

## How to Structure the `module_utils/` Directory

A typical `module_utils/` directory contains helper scripts used by custom modules:

```
module_utils/
├── common.py            # Shared helper functions
├── validation.py        # Data validation functions
```

## Creating a Shared Utility Module

Each script in `module_utils/` should contain reusable functions that can be imported into custom modules.

### Example: `module_utils/common.py`

```python
def format_output(name):
    return f"Hello, {name}!"
```

### Using the Utility Module in a Custom Module

Custom modules in `library/` can import these utilities.
Example: `library/custom_hello.py`

```python
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common import format_output

def run_module():
    module_args = dict(name=dict(type='str', required=True))
    module = AnsibleModule(argument_spec=module_args)
    result = format_output(module.params['name'])
    module.exit_json(changed=False, message=result)

if __name__ == '__main__':
    run_module()
```

## How Ansible Finds `module_utils/`

Ansible automatically looks for utilities in:

* **The `module_utils/` directory** within the role or project.
* **Globally configured paths** (set in `ANSIBLE_MODULE_UTILS`).

To verify that a module can import utilities correctly:

```bash
ansible-doc -t module -l
```

## Best Practices

* **Organize utilities by function** (e.g., `validation.py`, `network.py`).
* **Avoid circular dependencies** by keeping helper functions modular.
* **Document functions properly** for easier maintenance and reuse.
* **Test utilities separately** before integrating them into modules.

The `module_utils/` directory is a powerful tool for structuring reusable code in Ansible, enabling efficient and scalable module development.
