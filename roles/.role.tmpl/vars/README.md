# Ansible Vars Directory
roles/role_name/vars/README.md

## What is the `vars/` Directory?

The `vars/` directory in an Ansible project or role is used to **store variable definitions**.

## Why Use the `vars/` Directory?

* Centralizes variable management.
* Allows easy customization without editing playbooks.
* Enhances reusability by defining overridable values.

## How to Structure the `vars/` Directory

```
vars/
├── main.yml          # Primary variable file
├── app_config.yml    # Application variables
├── security.yml      # Security-related variables
```

## Defining Variables in `vars/`

Example: `vars/main.yml`

```yaml
dependency_packages:
  - curl
  - unzip
  - git

app_port: 8080
app_name: my_application
```

## Using Variables in Playbooks

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

## Overriding Variables

* `defaults/` variables have lowest priority.
* `vars/` variables override defaults.
* Extra vars from CLI have highest priority:

```bash
ansible-playbook playbook.yml -e "app_port=9090"
```

## Best Practices

* Prefer `defaults/` for general defaults; use `vars/` for role-specific overrides.
* Use descriptive names.
* Store secrets in Ansible Vault.
* Document important variables in `vars/main.yml`.
