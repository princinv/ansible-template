# Molecule Testing for Ansible Roles

## 📌 What is Molecule?
Molecule is a tool for **testing Ansible roles**. It helps ensure your roles work before applying them in production.

## 🔧 Installing Molecule
Run the setup script:
```bash
./setup.sh
```
This installs:
- **Molecule** (for role testing)
- **TestInfra** (for system verification)
- **Ansible Lint** (for best practices)

## 🚀 Running Molecule Tests
### 1️⃣ **Create a Test Environment**
```bash
molecule create
```
This launches a **Docker container** for testing.

### 2️⃣ **Apply the Role**
```bash
molecule converge
```
This runs the role **inside the test container**.

### 3️⃣ **Verify the Role Works**
```bash
molecule verify
```
This executes **TestInfra scripts** to check:
- If packages are installed.
- If services are running.
- If ports are open.

### 4️⃣ **Destroy the Test Environment**
```bash
molecule destroy
```
This removes the test container.

### 🔄 **Full Test Cycle**
Run **all steps automatically**:
```bash
molecule test
```
This:
1. Creates a test environment.
2. Applies the role.
3. Runs verification tests.
4. Cleans up.

## ✅ Example: Checking Python is Installed
Inside `tests/testinfra.py`:
```python
import testinfra

def test_python_installed(host):
    python = host.package("python3")
    assert python.is_installed
```
Run the test:
```bash
molecule verify
```
If it **fails**, something is wrong with the role.

---
## 🔍 Debugging
### SSH into the test container:
```bash
molecule login
```
Once inside, run:
```bash
systemctl status nginx
```
to check service status.

---
## 🏆 Why Use Molecule?
- 🛠 **Prevents configuration drift** by catching errors early.
- 🚀 **Automates testing** of Ansible roles.
- 🔍 **Ensures roles work before deploying** them to real servers.

