# Ansible Plugins Directory
plugins/README.md

## What is the `plugins/` Directory?

The `plugins/` directory in an Ansible project is used to **store custom plugins** that extend Ansible’s core functionality. Plugins can modify task execution, process data, enhance logging, or integrate with external systems.

## Why Use the `plugins/` Directory?

* **Expands Ansible’s capabilities** beyond built-in functions.
* **Supports custom logic** for specific automation needs.
* **Allows greater flexibility** in handling tasks, inventory, lookups, and callbacks.

## How to Structure the `plugins/` Directory

A typical `plugins/` directory contains different types of custom plugins:

```
plugins/
├── action_plugins/       # Custom action plugins that can modify the behavior of modules during execution.
├── become_plugins/       # Custom privilege escalation methods for controlling how Ansible becomes another user.
├── cache_plugins/        # Custom plugins for caching facts or other data between playbook runs.
├── callback_plugins/     # Custom logging, output formatting, and event callback plugins.
├── cliconf_plugins/      # Custom CLI protocol handlers for network devices using CLI-based APIs.
├── connection_plugins/   # Custom connection methods for managing how Ansible connects to target hosts.
├── doc_fragment_plugins/ # Shared documentation snippets for use in multiple plugins or modules.
├── filter_plugins/       # Custom Jinja2 filter plugins for use in templates and variables.
├── httpapi_plugins/      # Custom HTTP API protocol handlers for managing network devices via APIs.
├── inventory_plugins/    # Custom dynamic inventory source plugins for discovering and managing hosts.
├── lookup_plugins/       # Custom lookup plugins to retrieve external data for use in playbooks.
├── strategy_plugins/     # Custom execution strategies that control task execution order and parallelism.
├── terminal_plugins/     # Custom terminal handling for CLI connections, especially for network devices.
├── test_plugins/         # Custom Jinja2 test plugins for evaluating conditional expressions in templates.
├── vars_plugins/         # Custom plugins for manipulating or injecting variables into playbook execution.
```

## Creating a Custom Plugin

### Example: A Custom Lookup Plugin

A lookup plugin retrieves data dynamically.
Example: `plugins/lookup_plugins/custom_lookup.py`

```python
from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        return [term.upper() for term in terms]
```

### Using the Custom Lookup Plugin in a Playbook

```yaml
- name: Use a custom lookup
  debug:
    msg: "{{ lookup('custom_lookup', 'hello', 'world') }}"
```

**Output:** `["HELLO", "WORLD"]`

## Where Ansible Looks for Plugins

By default, Ansible searches for plugins in:

* **The `plugins/` directory** at the same level as the playbook.
* **Global plugin directories** configured via `ANSIBLE_LIBRARY`.

To list available plugins:

```bash
ansible-doc -t lookup -l
```

## Best Practices

* **Keep plugins organized** by type (e.g., lookup, callback, action).
* **Ensure plugins are efficient** to avoid slowing down playbook execution.
* **Use descriptive names** to prevent conflicts with built-in Ansible plugins.
* **Test plugins separately** before integrating them into playbooks.

The `plugins/` directory enables advanced customization, allowing Ansible users to extend automation workflows with specialized functionality.
