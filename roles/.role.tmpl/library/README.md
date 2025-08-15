# Ansible Library Directory
roles/role_name/library/README.md

## What is the `library/` Directory?

The `library/` directory in an Ansible project or role is used to **store custom Ansible modules**.

## Why Use the `library/` Directory?

* Enables custom functionality beyond built-in modules.
* Allows reuse of custom scripts across roles/playbooks.
* Works seamlessly with Ansible.

## How to Structure the `library/` Directory

```
library/
├── custom_hello.py
├── advanced_module.py
```

## Creating a Custom Module

```python
#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        name=dict(type='str', required=True)
    )
    module = AnsibleModule(argument_spec=module_args)
    result = {"message": f"Hello, {module.params['name']}!"}
    module.exit_json(changed=False, result=result)

if __name__ == '__main__':
    run_module()
```

## Using the Custom Module

```yaml
- name: Say Hello
  custom_hello:
    name: "Homelab"
  register: result

- debug:
    msg: "{{ result.result.message }}"
```

**Output:** `Hello, Homelab!`

## Best Practices

* Use descriptive function names.
* Keep modules simple.
* Test modules separately.
* Use `module_utils/` for shared functions.
