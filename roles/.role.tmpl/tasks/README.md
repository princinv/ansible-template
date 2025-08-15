# Ansible Tasks Directory
roles/role_name/tasks/README.md

## What is the `tasks/` Directory?

The `tasks/` directory in an Ansible role is used to **store task definitions**, which are the core execution units of Ansible automation.

## Why Use the `tasks/` Directory?

* Defines automation logic for configuring systems.
* Organizes tasks in modular files for better readability and maintainability.
* Facilitates reusability by structuring role execution clearly.

## How to Structure the `tasks/` Directory

```
tasks/
├── main.yml          # Primary entry point for tasks
├── install.yml       # Tasks related to software installation
├── configure.yml     # Configuration-related tasks
├── service.yml       # Tasks for managing services
```

## Defining Tasks in `tasks/`

Example: `tasks/main.yml`

```yaml
- name: Include installation tasks
  ansible.builtin.include_tasks: install.yml

- name: Include configuration tasks
  ansible.builtin.include_tasks: configure.yml

- name: Include service management tasks
  ansible.builtin.include_tasks: service.yml
```

Example: `tasks/install.yml`

```yaml
- name: Install required packages
  ansible.builtin.apt:
    name: "{{ dependency_packages }}"
    state: present
```

## Using the `tasks/` Directory in Playbooks

```yaml
- name: Apply example role
  hosts: all
  become: true
  roles:
    - example_role
```

## Best Practices

* Keep `tasks/main.yml` as an entry point.
* Use meaningful task names for easy debugging.
* Break down complex playbooks with `include_tasks` and `import_tasks`.
* Ensure tasks are idempotent.
* Test execution with `--check` before applying changes.
