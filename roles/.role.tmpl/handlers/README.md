
# Ansible Handlers Directory
roles/role_name/handlers/README.md

## What is the `handlers/` Directory?

The `handlers/` directory in an Ansible role is used to store **handlers**, which are special tasks that are triggered only when notified by other tasks.

## Why Use the `handlers/` Directory?

* Ensures tasks are only executed when necessary.
* Enhances efficiency by preventing redundant service restarts or reloads.
* Keeps playbooks modular.

## How to Use the `handlers/` Directory

### Defining a Handler

Example: `handlers/main.yml`

```yaml
- name: Restart Nginx
  ansible.builtin.service:
    name: nginx
    state: restarted
```

### Calling a Handler from a Task

```yaml
- name: Update Nginx configuration
  ansible.builtin.copy:
    src: files/nginx.conf
    dest: /etc/nginx/nginx.conf
  notify: Restart Nginx
```

**The handler runs only if this task changes the file.**

### Using Multiple Handlers

```yaml
- name: Deploy configuration
  ansible.builtin.template:
    src: templates/app.conf.j2
    dest: /etc/app.conf
  notify:
    - Restart App Service
    - Reload Systemd
```

## When Do Handlers Execute?

Handlers execute at the end of a play unless explicitly forced with:

```yaml
- meta: flush_handlers
```

## Best Practices

* Use handlers for restarts/reloads.
* Keep handler names descriptive.
* Group similar handlers in one file.
* Avoid `flush_handlers` unless necessary.
