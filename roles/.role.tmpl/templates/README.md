# Ansible Templates Directory

## 📌 What is the `templates/` Directory?
The `templates/` directory in an Ansible project or role is used to **store Jinja2 template files** that allow for dynamic content generation.

## 📦 Why Use the `templates/` Directory?
- 🛠 **Dynamically generates configuration files** using variables.
- 🔄 **Enables flexible automation** by adapting templates to different environments.
- 🚀 **Reduces redundancy** by allowing reuse of template files across multiple systems.

## 📄 How to Structure the `templates/` Directory
A typical `templates/` directory contains Jinja2 (`.j2`) template files:
```
templates/
├── nginx.conf.j2         # Nginx configuration template
├── motd.j2              # Dynamic Message of the Day (MOTD)
├── app_config.yaml.j2   # Application-specific configuration
```

## 🔍 Creating a Jinja2 Template
Templates use **Jinja2 syntax** to insert dynamic values.

### 🔹 Example: `templates/nginx.conf.j2`
```nginx
server {
    listen 80;
    server_name {{ server_name }};

    location / {
        proxy_pass http://{{ backend_host }}:{{ backend_port }};
    }
}
```

## 🚀 Using Templates in Playbooks
The `template` module is used to process Jinja2 templates and copy them to remote hosts.

### 🔹 Example: Applying a Template in a Playbook
```yaml
- name: Deploy Nginx Configuration
  ansible.builtin.template:
    src: templates/nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    owner: root
    group: root
    mode: '0644'
```
✅ **Ansible replaces `{{ server_name }}`, `{{ backend_host }}`, and `{{ backend_port }}` with actual values.**

### 🔹 Example: Supplying Variables to a Template
Variables can be defined in `group_vars/`, `host_vars/`, or inline:
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

## 🏆 Best Practices
- **Use `.j2` as the file extension** to distinguish templates from static files.
- **Keep template logic simple**—avoid complex conditionals when possible.
- **Use default values in variables** to prevent undefined errors.
- **Ensure proper permissions** when deploying sensitive files.
- **Validate rendered templates** before applying them to production systems:
  ```bash
  ansible-playbook --check --diff playbook.yml
  ```

The `templates/` directory is a powerful tool in Ansible automation, enabling dynamic configuration management tailored to different environments.

