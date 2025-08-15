# Ansible Files Directory
files/README.md

## What is the `files/` Directory?

The `files/` directory in an Ansible role or playbook is used to store **static files** that need to be copied to remote hosts. Unlike templates, these files are not dynamically modified by Ansible before deployment.

## Why Use the `files/` Directory?

* **Stores static files** such as configuration files, certificates, and scripts.
* **Ensures idempotency** by keeping known-good file versions.
* **Works with Ansible's `copy` and `file` modules** for transferring files to remote systems.

## How to Use the `files/` Directory

### Copying a File to a Remote Host

Use the `copy` module to transfer a file:

```yaml
- name: Copy an Nginx configuration file
  ansible.builtin.copy:
    src: files/nginx.conf
    dest: /etc/nginx/nginx.conf
    owner: root
    group: root
    mode: '0644'
```

**`src:` references the `files/` directory within the role/playbook.**

### Ensuring a File Exists but Not Modifying Content

Use the `file` module to check for a file’s existence:

```yaml
- name: Ensure a log file exists
  ansible.builtin.file:
    path: /var/log/myapp.log
    state: touch
    mode: '0644'
```

### Transferring Binary Files

Binary files (e.g., `.tar.gz`, `.pem`, `.zip`) can be stored in `files/` and copied over without modification:

```yaml
- name: Deploy an SSL certificate
  ansible.builtin.copy:
    src: files/ssl/cert.pem
    dest: /etc/ssl/certs/cert.pem
    owner: root
    group: root
    mode: '0600'
```

## When to Use `files/` vs. `templates/`

| Feature       | `files/` (Static Files) | `templates/` (Dynamic Templates) |
| ------------- | ----------------------- | -------------------------------- |
| **File Type** | Predefined, unmodified  | Jinja2 templates with variables  |
| **Use Case**  | Certs, scripts, configs | Configs needing templating logic |
| **Example**   | `.pem`, `.conf`, `.sh`  | `nginx.conf.j2`, `motd.j2`       |

## Best Practices

* **Use `files/` for unchanging static files**.
* **Use `templates/` for configurations requiring dynamic values**.
* **Set correct permissions** when copying sensitive files (e.g., `mode: '0600'` for private keys).
* **Avoid hardcoding paths**; use variables where possible (e.g., \`dest: "{{ nginx\_config\_path }}/nginx.conf"").

The `files/` directory ensures reliable, repeatable deployments of necessary static assets across your infrastructure.