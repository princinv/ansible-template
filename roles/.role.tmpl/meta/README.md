# Ansible Meta Directory
roles/role_name/meta/README.md

## What is the `meta/` Directory?

The `meta/` directory in an Ansible role is used to **store metadata about the role**.

## Why Use the `meta/` Directory?

* Defines role dependencies.
* Provides metadata for Ansible Galaxy.
* Ensures compatibility.

## Structure

```
meta/
├── main.yml
```

## Example `meta/main.yml`

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

## Best Practices

* Define dependencies explicitly.
* Include meaningful tags.
* Specify supported platforms.
* Keep metadata updated.
