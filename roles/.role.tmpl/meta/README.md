# Ansible Meta Directory

## 📌 What is the `meta/` Directory?
The `meta/` directory in an Ansible role is used to **store metadata about the role**, such as dependencies, author information, and role versions.

## 📦 Why Use the `meta/` Directory?
- 🛠 **Defines role dependencies** to automatically install required roles.
- 🔄 **Provides metadata for Ansible Galaxy** when sharing roles.
- 🚀 **Ensures compatibility** by specifying minimum Ansible versions.

## 📄 How to Structure the `meta/` Directory
A typical `meta/` directory contains a single YAML file:
```
meta/
├── main.yml  # Role metadata and dependencies
```

## 🔍 Defining Role Metadata
### 🔹 Example: `meta/main.yml`
```yaml
galaxy_info:
  author: your_name
  description: Example role for configuring a web server
  company: your_company
  license: MIT
  min_ansible_version: 2.9
  platforms:
    - name: Ubuntu
      versions:
        - 20.04
        - 22.04
  galaxy_tags:
    - web
    - nginx
    - server

dependencies:
  - role: common
```

## 🚀 How Ansible Uses the `meta/` Directory
### 🔹 Installing Role Dependencies
If a role has dependencies listed in `meta/main.yml`, they can be installed automatically:
```bash
ansible-galaxy install -r requirements.yml
```

### 🔹 Specifying Role Dependencies in `requirements.yml`
```yaml
roles:
  - name: example_role
    src: https://github.com/example/example_role.git
    version: main
```

## 🏆 Best Practices
- **Define dependencies** explicitly to avoid missing requirements.
- **Include meaningful tags** for Ansible Galaxy to improve discoverability.
- **Specify supported platforms** to clarify role compatibility.
- **Keep metadata up to date** when modifying the role.

The `meta/` directory ensures that Ansible roles are well-documented, compatible, and properly structured for sharing and automation.

