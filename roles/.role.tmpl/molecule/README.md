# Molecule Testing for Ansible Roles
roles/role_name/molecule/README.md

## What is Molecule?

Molecule is a tool for **testing Ansible roles**.

## Installing Molecule

```bash
./setup.sh
```

Installs:

* Molecule
* TestInfra
* Ansible Lint

## Running Molecule Tests

### Create Test Environment

```bash
molecule create
```

### Apply the Role

```bash
molecule converge
```

### Verify Role Works

```bash
molecule verify
```

### Destroy Test Environment

```bash
molecule destroy
```

### Full Test Cycle

```bash
molecule test
```

## Example Test

```python
import testinfra

def test_python_installed(host):
    python = host.package("python3")
    assert python.is_installed
```

Run:

```bash
molecule verify
```

## Best Practices

* Test early and often.
* Use Molecule to validate before production.
* Debug by logging into test containers with `molecule login`.
