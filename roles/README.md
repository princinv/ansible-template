# Ansible Roles Directory
roles/README.md

## What is the `roles/` Directory?

The `roles/` directory in an Ansible project stores **reusable role definitions**. Each role is a self-contained unit that can include tasks, handlers, templates, variables, and other components needed for automation.

## Why Use the `roles/` Directory?

* **Encapsulates automation logic** into structured, reusable components.
* **Separates concerns** by organizing tasks, variables, and templates per role.
* **Enables modular automation** that can be applied across multiple playbooks.

## Structure of the `roles/` Directory

A typical `roles/` directory contains multiple structured roles, each following the same internal layout:

```
roles/
├── common/              # Example role for system-wide configurations
│   ├── defaults/        # Default variable values (lowest precedence)
│   ├── vars/            # Role-specific variables (higher precedence)
│   ├── tasks/           # Main role logic
│   │   ├── main.yml     # Auto-loaded task file
│   ├── handlers/        # Handlers for event-driven actions
│   ├── templates/       # Jinja2 templates for dynamic configs
│   ├── files/           # Static files to be copied to hosts
│   ├── library/         # Custom modules for this role
│   ├── meta/            # Role metadata (dependencies, author info)
│   ├── molecule/        # Molecule testing framework for the role
│   ├── tests/           # Automated tests for the role
│   ├── docs/            # Role-specific documentation
│   └── README.md        # Role-level documentation
```

## Creating a Role

Roles can be created with the `ansible-galaxy` command:

```bash
ansible-galaxy init roles/example_role
```

This generates a role skeleton with the correct directory structure.

### Example: `roles/common/tasks/main.yml`

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

## Using Roles in Playbooks

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

## Best Practices

* **Use `defaults/` for role-wide defaults** to keep playbooks flexible.
* **Document role variables** in `defaults/main.yml` and `vars/main.yml`.
* **Define `meta/main.yml`** to specify dependencies.
* **Organize tasks logically** in `tasks/main.yml` and split complex logic into smaller files.
* **Test roles with Molecule** to ensure reliability before deployment.

The `roles/` directory is the foundation of scalable Ansible automation, enabling efficient reuse, maintainability, and consistency across multiple projects.
