# Ansible Templates Directory
roles/role_name/templates/README.md

## What is the `templates/` Directory?

The `templates/` directory in an Ansible project or role is used to **store Jinja2 template files** for dynamic content generation.

## Why Use the `templates/` Directory?

* Dynamically generates configuration files using variables.
* Enables flexible automation by adapting templates to different environments.
* Reduces redundancy by allowing reuse of template files.

## How to Structure the `templates/` Directory

```
templates/
├── nginx.conf.j2         # Nginx configuration template
├── motd.j2               # Dynamic MOTD
├── app_config.yaml.j2    # Application configuration
```

## Creating a Jinja2 Template

Example: `templates/nginx.conf.j2`

```nginx
server {
    listen 80;
    server_name {{ server_name }};

    location / {
        proxy_pass http://{{ backend_host }}:{{ backend_port }};
    }
}
```

## Using Templates in Playbooks

```yaml
- name: Deploy Nginx Configuration
  ansible.builtin.template:
    src: templates/nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    owner: root
    group: root
    mode: '0644'
```

Example with Variables:

```yaml
- name: Apply Nginx Template with Variables
  hosts: web_servers
  vars:
    server_name: example.com
    backend_host: 192.168.1.10
    backend_port: 8080
  tasks:
    - name: Deploy Nginx Config
      ansible.builtin.template:
        src: templates/nginx.conf.j2
        dest: /etc/nginx/nginx.conf
```

## Best Practices

* Use `.j2` extension for templates.
* Keep template logic simple.
* Use default values to avoid undefined errors.
* Apply correct permissions.
* Validate templates before production deployment.
