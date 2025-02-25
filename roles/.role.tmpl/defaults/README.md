# Ansible Defaults Directory

## 📌 What is the `defaults/` Directory?
The `defaults/` directory in an Ansible role is used to **store default variable values** that can be overridden by higher-priority variables.

## 📦 Why Use the `defaults/` Directory?
- 🛠 **Provides default values** for role variables, ensuring playbooks run with sensible settings.
- 🔄 **Allows easy overrides** via `vars/`, inventory files, or command-line extra vars.
- 🚀 **Improves reusability** by defining role-wide defaults without enforcing strict values.

## 📄 How to Structure the `defaults/` Directory
A typical `defaults/` directory contains a single YAML file:
```
defaults/
├── main.yml  # Default variable definitions
```

## 🔍 Defining Default Variables
### 🔹 Example: `defaults/main.yml`
```yaml
dependency_packages:
  - curl
  - unzip
  - git

app_port: 8080
app_name: my_application
```

## 🚀 Using Default Variables in Playbooks
Default variables from `defaults/` can be referenced in tasks:
```yaml
- name: Install required packages
  ansible.builtin.apt:
    name: "{{ dependency_packages }}"
    state: present

- name: Configure application
  ansible.builtin.template:
    src: templates/app_config.j2
    dest: /etc/app/config.yml
```

## 🔹 Overriding Default Variables
Default variables in `defaults/` can be overridden by:
1. **Inventory variables** (higher priority than defaults)
2. **`vars/` variables** (higher priority than inventory variables)
3. **Command-line extra vars (highest priority)**:
   ```bash
   ansible-playbook playbook.yml -e "app_port=9090"
   ```

## 🏆 Best Practices
- **Use `defaults/` for role-wide default values** to allow flexibility in overrides.
- **Keep variables generic and non-enforcing**, ensuring easy customization.
- **Avoid hardcoded credentials or sensitive data**, instead use **Ansible Vault**.
- **Document default values** within `defaults/main.yml` for clarity.

The `defaults/` directory ensures Ansible roles are reusable and adaptable by defining sensible starting values that can be customized when needed.

