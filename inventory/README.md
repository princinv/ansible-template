# Ansible Inventory Directory
inventory/README.md

## What is the `inventory/` Directory?

The `inventory/` directory in an Ansible project is used to **define and manage the target hosts** for automation. It contains **inventory files** that specify groups of hosts and their associated variables.

## Why Use the `inventory/` Directory?

* **Defines target systems** that Ansible manages.
* **Groups hosts logically** (e.g., web servers, databases, proxies).
* **Stores per-group and per-host variables** for flexibility.

## How to Structure the `inventory/` Directory

A typical `inventory/` directory contains:

```
inventory/
├── hosts.yml         # Main inventory file
├── group_vars/       # Group-wide variables
│   ├── all.yml       # Variables for all hosts
│   ├── web.yml       # Variables for web servers
│   ├── db.yml        # Variables for database servers
├── host_vars/        # Per-host specific variables
│   ├── web1.yml      # Variables for web1
│   ├── db1.yml       # Variables for db1
```

## How to Define an Inventory

Ansible supports inventories in **YAML, INI, and dynamic formats**.

### Example: `inventory/hosts.yml`

```yaml
all:
  children:
    web_servers:
      hosts:
        web1:
          ansible_host: 192.168.1.10
        web2:
          ansible_host: 192.168.1.11
    db_servers:
      hosts:
        db1:
          ansible_host: 192.168.1.20
```

### Using `group_vars/` for Group-Wide Settings

Example: `inventory/group_vars/web.yml`

```yaml
ansible_user: ubuntu
ansible_ssh_private_key_file: ~/.ssh/id_rsa
web_service_port: 80
```

### Using `host_vars/` for Per-Host Settings

Example: `inventory/host_vars/web1.yml`

```yaml
custom_hostname: web1-production
web_service_port: 8080
```

## Using the Inventory in Playbooks

Once defined, the inventory can be used in playbooks:

```yaml
- name: Deploy web servers
  hosts: web_servers
  tasks:
    - name: Install Nginx
      ansible.builtin.apt:
        name: nginx
        state: present
```

## Best Practices

* **Use `group_vars/` and `host_vars/`** to avoid hardcoded values in playbooks.
* **Separate inventories** for different environments (e.g., `inventory/dev/`, `inventory/prod/`).
* **Use dynamic inventories** if managing cloud-based or dynamic hosts.
* **Keep hostnames meaningful** (e.g., `web1`, `db1` instead of `host1`, `host2`).

The `inventory/` directory is critical for organizing and managing hosts efficiently, enabling structured and scalable automation with Ansible.