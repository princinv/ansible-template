# Ansible Tests Directory
roles/role_name/test/README.md

## What is the `tests/` Directory?

The `tests/` directory in an Ansible project or role is used to **store test cases and validation scripts**.

## Why Use the `tests/` Directory?

* Automates validation of roles and playbooks.
* Prevents configuration drift.
* Enhances reliability through structured testing.

## How to Structure the `tests/` Directory

```
tests/
├── test.yml           # Ansible test playbook
├── testinfra/         # Python-based infrastructure tests
│   ├── test_default.py
├── molecule/          # Molecule testing framework (if used)
```

## Creating an Ansible Test Playbook

Example: `tests/test.yml`

```yaml
- name: Test Role Execution
  hosts: all
  become: true
  roles:
    - example_role
```

Run:

```bash
ansible-playbook tests/test.yml --check --diff
```

## Using TestInfra for Validation

Example: `tests/testinfra/test_default.py`

```python
import testinfra

def test_nginx_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed

def test_nginx_running(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled
```

Run:

```bash
pytest -v tests/testinfra/
```

## Best Practices

* Use `tests/` for structured validation.
* Combine Ansible check mode with test playbooks.
* Use Molecule for isolated testing.
* Focus tests on critical services/configurations.
