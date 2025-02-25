# Ansible Library Directory

## 📌 What is the `library/` Directory?
The `library/` directory in an Ansible project or role is used to **store custom Ansible modules**. These modules extend Ansible’s core functionality when built-in modules do not meet specific needs.

## 📦 Why Use the `library/` Directory?
- 🛠 **Enables custom functionality** beyond Ansible’s built-in modules.
- 🚀 **Allows for reuse of custom scripts** across different roles and playbooks.
- 🔄 **Works seamlessly with Ansible** as it auto-loads modules from this directory.

## 📄 How to Structure the `library/` Directory
A typical `library/` directory contains custom modules:
```
library/
├── custom_hello.py        # Example: A simple custom module
├── advanced_module.py     # More complex functionality
```

## 🔍 Creating a Custom Module
Each module is a Python script implementing `AnsibleModule` from `ansible.module_utils.basic`.

### 🔹 Example: `library/custom_hello.py`
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

## 🚀 Using the Custom Module in a Playbook
Once placed in the `library/` directory, the module can be used like any built-in module:
```yaml
- name: Say Hello
  custom_hello:
    name: "Homelab"
  register: result

- debug:
    msg: "{{ result.result.message }}"
```
✅ **Output:** `"Hello, Homelab!"`

## 🔍 Where Ansible Looks for Custom Modules
By default, Ansible searches for modules in:
- **The `library/` directory** at the same level as the playbook.
- **Globally configured paths** (set in `ANSIBLE_LIBRARY`).

To verify available modules:
```bash
ansible-doc -l | grep custom_
```

## 🏆 Best Practices
- **Use descriptive function names** to improve readability.
- **Keep modules simple and focused** for easier debugging.
- **Test modules separately** before integrating them into playbooks.
- **Use `module_utils/`** for shared helper functions when writing complex modules.

The `library/` directory is a powerful way to extend Ansible’s automation capabilities, allowing for tailored functionality to meet unique operational requirements.

