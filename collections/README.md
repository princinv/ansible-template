# Ansible Collections
collections/README.md

## What are Collections?

Ansible Collections are a way to **package and distribute modules, roles, and plugins** together in a structured format. They allow for easier reuse and organization of automation components.

## Why Use Collections?

* **Simplifies role and module management** by grouping related content.
* **Encapsulates dependencies** so everything needed for a task is packaged together.
* **Enables versioning and sharing** across teams or the Ansible Galaxy community.

## Installing Collections

To install a collection from **Ansible Galaxy**, use:

```bash
ansible-galaxy collection install community.general
```

To install collections defined in `requirements.yml`, run:

```bash
ansible-galaxy collection install -r requirements.yml
```

## Example: `requirements.yml`

```yaml
collections:
  - name: community.general
  - name: ansible.posix
```

This ensures the necessary collections are installed before running playbooks.

## Where Are Collections Stored?

By default, collections are installed in:

* **`~/.ansible/collections/`** (for a single user)
* **`/usr/share/ansible/collections/`** (system-wide)

You can also specify a custom location in **`ansible.cfg`**:

```ini
[defaults]
collections_path = ./collections
```

## Using a Collection in Playbooks

Once installed, use a collection module like this:

```yaml
- name: Use a module from a collection
  community.general.ping:
```

This references the `ping` module from the `community.general` collection.

## Best Practices

* **Specify collection versions** in `requirements.yml` for consistency.
* **Use collections in roles** to keep playbooks clean and modular.
* **Check for updates** periodically using:

  ```bash
  ansible-galaxy collection list
  ```

Ansible Collections streamline automation by bundling related components into reusable, version-controlled packages.