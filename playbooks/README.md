# Ansible Playbooks Directory
playbooks/README.md

## What is the `playbooks/` Directory?

The `playbooks/` directory in an Ansible project is used to **store individual playbooks** that define automation tasks for managing systems and applications.

## Why Use the `playbooks/` Directory?

* **Keeps playbooks organized** in a central location.
* **Separates logic from roles**, allowing reuse across multiple environments.
* **Facilitates structured automation** by maintaining clear, modular workflows.

## How to Structure the `playbooks/` Directory

A typical `playbooks/` directory contains structured playbooks:

```
playbooks/
├── site.yml               # Main playbook including all others
├── docker-deploy.yml      # Deploys Docker containers
├── proxmox-config.yml     # Configures Proxmox settings
├── security-hardening.yml # Security configurations
├── monitoring.yml         # Installs and configures monitoring tools
```

## Creating a Playbook

Playbooks are YAML files that define automation steps for managed hosts.

### Example: `playbooks/site.yml`

```yaml
- name: Configure all servers
  hosts: all
  become: true
  roles:
    - common
    - security
    - monitoring
```

### Running a Playbook

To execute a playbook, use:

```bash
ansible-playbook playbooks/site.yml
```

### Using Tags for Selective Execution

Tags allow you to run specific parts of a playbook:

```yaml
- name: Install and configure Nginx
  hosts: web_servers
  tasks:
    - name: Install Nginx
      ansible.builtin.apt:
        name: nginx
        state: present
      tags:
        - install

    - name: Start Nginx
      ansible.builtin.service:
        name: nginx
        state: started
      tags:
        - start
```

Run only the `install` tasks:

```bash
ansible-playbook playbooks/site.yml --tags install
```

## Best Practices

* **Use `site.yml` as the main entry point**, including all other playbooks.
* **Keep playbooks modular**, separating concerns (e.g., security, monitoring, deployments).
* **Leverage roles** to encapsulate reusable configurations.
* **Use tags** for flexibility in execution.
* **Maintain consistency in naming** (e.g., `playbooks/docker-deploy.yml`).

The `playbooks/` directory provides a structured approach to automation, ensuring clarity, maintainability, and scalability in Ansible workflows.
