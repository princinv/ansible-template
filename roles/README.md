# Ansible Roles Directory

## 📌 What is the `roles/` Directory?
The `roles/` directory in an Ansible project is used to **store reusable role definitions** that contain tasks, handlers, templates, variables, and other components necessary for automation.

## 📦 Why Use the `roles/` Directory?
- 🛠 **Encapsulates automation logic** into structured, reusable components.
- 🔄 **Separates concerns** by organizing tasks, variables, and templates per role.
- 🚀 **Enables modular automation** that can be applied across different playbooks.

## 📄 How to Structure the `roles/` Directory
A typical `roles/` directory contains multiple structured roles:
```
roles/
├── common/              # Base role for system-wide configurations
│   ├── tasks/          # Main role logic
│   │   ├── main.yml    # Auto-loaded task file
│   ├── handlers/       # Handlers for restarting services
│   ├── templates/      # Jinja2 templates for dynamic configs
│   ├── files/          # Static files to be copied
│   ├── vars/           # Role-specific variables
│   ├── defaults/       # Default variable values
│   ├── meta/           # Role metadata (dependencies, author info)
│   ├── tests/          # Automated tests for the role
│   ├── molecule/       # Molecule testing framework for the role
```

## 🔍 Creating a Role
Roles are created using the `ansible-galaxy` command:
```bash
ansible-galaxy init roles/example_role
```
This generates a structured role skeleton inside `roles/`.

### 🔹 Example: `roles/common/tasks/main.yml`
```yaml
- name: Ensure Nginx is installed
  ansible.builtin.apt:
    name: nginx
    state: present

- name: Start Nginx service
  ansible.builtin.service:
    name: nginx
    state: started
    enabled: true
```

## 🚀 Using Roles in Playbooks
Once defined, roles can be included in playbooks:
```yaml
- name: Apply roles to servers
  hosts: all
  become: true
  roles:
    - common
    - security
    - monitoring
```

## 🏆 Best Practices
- **Use `defaults/` for role-wide variable defaults** to keep playbooks flexible.
- **Define `meta/main.yml`** to specify dependencies between roles.
- **Organize tasks logically** inside `tasks/main.yml` and split complex logic into separate files.
- **Test roles using Molecule** to ensure reliability before deployment.

The `roles/` directory is the foundation of scalable Ansible automation, allowing efficient reuse and maintainability across multiple projects.

