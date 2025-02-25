# Ansible Tests Directory

## 📌 What is the `tests/` Directory?
The `tests/` directory in an Ansible project or role is used to **store test cases and validation scripts** to ensure that playbooks and roles work as expected.

## 📦 Why Use the `tests/` Directory?
- 🛠 **Automates validation** of roles and playbooks before deployment.
- 🔄 **Prevents configuration drift** by catching issues early.
- 🚀 **Enhances reliability** through structured testing.

## 📄 How to Structure the `tests/` Directory
A typical `tests/` directory contains:
```
tests/
├── test.yml           # Ansible test playbook
├── testinfra/         # Python-based infrastructure tests
│   ├── test_default.py
├── molecule/          # Molecule testing framework (if used)
```

## 🔍 Creating an Ansible Test Playbook
A simple test playbook ensures that a role executes without errors.

### 🔹 Example: `tests/test.yml`
```yaml
- name: Test Role Execution
  hosts: all
  become: true
  roles:
    - example_role
```

Run the test playbook:
```bash
ansible-playbook tests/test.yml --check --diff
```

## 🚀 Using TestInfra for Validation
TestInfra allows Python-based assertions to verify system state.

### 🔹 Example: `tests/testinfra/test_default.py`
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

Run TestInfra tests:
```bash
pytest -v tests/testinfra/
```

## 🏆 Best Practices
- **Use `tests/` for structured validation** before applying roles/playbooks in production.
- **Combine Ansible check mode (`--check`) with test playbooks** for dry runs.
- **Use Molecule for role testing** to automate execution in isolated environments.
- **Ensure test cases are meaningful**—focus on critical services and configurations.

The `tests/` directory is essential for maintaining reliable and reproducible Ansible automation workflows.

