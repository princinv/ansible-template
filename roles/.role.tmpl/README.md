roles/role_name/README.md

# role_name

## Description

This role configures **role_name** for the homelab. It follows a consistent structure based on the `.role.tmpl` template to ensure maintainability, readability, and testability.

## Requirements

* Ansible >= 2.14
* Python >= 3.9
* Recommended: Molecule, TestInfra, and Ansible Lint for testing and validation.

## Role Structure

The role is generated from `.role.tmpl` and contains the following directories:

```
roles/{{ role_name }}/
├── defaults/       # Default variable values (overridable)
├── docs/           # Additional role-specific documentation
├── handlers/       # Event-driven tasks triggered by notifications
├── library/        # Custom Ansible modules for this role
├── meta/           # Role metadata and dependencies
├── molecule/       # Molecule configuration for testing
├── tasks/          # Main task definitions (core logic)
├── templates/      # Jinja2 templates for dynamic file generation
├── tests/          # Test playbooks and supporting files
├── vars/           # Role-specific variables (higher precedence than defaults)
└── README.md       # Role-level documentation
```

Each major subdirectory (except `docs/`) contains its own `README.md` explaining its purpose and best practices.

## Role Variables

All role variables are documented in:

* `defaults/main.yml` — Base defaults for the role.
* `vars/main.yml` — Higher precedence variables for role-specific overrides.

Document each variable here, including its default value, description, and example overrides.

Example:

```yaml
app_port: 8080        # Port on which the application listens
app_name: myapp       # Name of the application
```

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:
    - role: {{ role_name }}
```

## Testing the Role

Molecule is pre-configured for testing this role.

### Run full test cycle:

```bash
molecule test
```

### Run only converge step:

```bash
molecule converge
```

### Log into the test instance:

```bash
molecule login
```

## CI/CD and Linting

Ansible Lint configurations are included for consistency across CI/CD pipelines.
Run:

```bash
ansible-lint
```

## Notes on `.role.tmpl`

When you run:

```bash
ansible-galaxy init myrole
```

you can copy or link files from `.role.tmpl` to create a fully structured role. Placeholders like `{{ role_name }}` should be updated manually or pre-processed with a one-liner.

### Benefits of `.role.tmpl`

* Ensures **consistent layout** across all roles.
* Includes **README.md** for each major subdirectory.
* Ready-to-use **Molecule** tests.
* Pre-configured **linting** for CI/CD workflows.
* Encourages **modularity and reusability** in role design.

---

This README serves as the primary documentation for the role. Refer to individual directory README files for details on their specific purposes and usage.
