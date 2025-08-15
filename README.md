# Ansible-Template
<img src="https://raw.githubusercontent.com/princinv/assets/main/ansible-master_banner.png" alt="Dotfiles Banner" width="100%" />
---

__much thanks to (@geerlingguy)[https://github.com/geerlingguy] for the great materials on using ansible.__

**WIP**

A complete template of default digestible directory structures in Ansible playbook. 

With some customizations. 

## RESOURCES



## FOLDER STRUCTURE

```markdown
playbook-template/
├── collections/                 # Custom or vendored Ansible collections
│   └── README.md
├── files/                       # Global static files (configs, certs, etc.)
│   └── README.md
├── handlers/                    # Global handlers for event-driven tasks
│   ├── main.yml
│   └── README.md
├── inventory/                   # Host and variable definitions
│   ├── DEFAULT_VARS.md          # Documentation for default inventory variables
│   ├── hosts.yml                 # Main inventory file
│   ├── group_vars/              # Variables for host groups (auto-loaded)
│   │   └── all/
│   │       └── all.yml
│   ├── host_vars/               # Variables for individual hosts (auto-loaded)
│   │   └── hostname/
│   │       └── hostname.yml
│   └── README.md
├── library/                     # Custom Ansible modules
│   └── README.md
├── log/                         # Centralized logging directory
│   └── README.md
├── module_utils/                 # Shared Python utilities for custom modules
│   └── README.md
├── playbooks/                   # Standalone playbooks
│   ├── site.yml                  # Main site playbook
│   ├── trigger_callback.yml      # Example callback trigger playbook
│   └── README.md
├── plugins/                      # Custom plugins to extend Ansible
│   ├── action_plugins/
│   ├── become_plugins/
│   ├── cache_plugins/
│   ├── callback_plugins/
│   │   ├── bootstrap.py
│   │   └── README.md
│   ├── cliconf_plugins/
│   ├── connection_plugins/
│   ├── doc_fragment_plugins/
│   ├── filter_plugins/
│   │   ├── filters.py
│   │   └── README.md
│   ├── httpapi_plugins/
│   ├── inventory_plugins/
│   ├── lookup_plugins/
│   │   └── README.md
│   ├── strategy_plugins/
│   ├── terminal_plugins/
│   ├── test_plugins/
│   └── vars_plugins/
│   └── README.md
├── roles/                        # Modular, reusable role definitions
│   └── README.md                  # Documentation for roles directory
├── templates/                     # Global Jinja2 templates
│   └── README.md
├── tests/                         # Global playbook/role tests
│   └── README.md
├── vars/                          # Global variable definitions
│   └── README.md
├── ansible.cfg                  # Ansible configuration file
├── ansible.cfg.tmpl             # Template for ansible.cfg (for customization)
├── bootstrap.sh                 # Script to prepare the execution environment
├── README.md                     # Project-level documentation
├── requirements.txt              # Python dependencies
└── requirements.yml               # Ansible Galaxy dependencies (roles/collections)
 ```


## Directory Information

| Directory         | **Role-Level Only** | **Playbook-Level Only** | **Both** | **Notes** |
|-------------------|---------------------|-------------------------|----------|-----------|
| `collections/`    | ❌ | ✅ | ❌ | Stores Ansible collections installed from Galaxy or Git. |
| `defaults/`       | ✅ | ❌ | ❌ | Lowest priority variables; intended for safe defaults. |
| `files/`          | ❌ | ✅ | ❌ | Static files copied as-is to hosts. |
| `handlers/`       | ✅ | ✅ | ✅ | Event-driven tasks triggered by `notify`. |
| `inventory/`      | ❌ | ✅ | ❌ | Host and group definitions, plus variables. |
| `library/`        | ✅ | ✅ | ✅ | Custom Ansible modules. |
| `meta/`           | ✅ | ❌ | ❌ | Role metadata, dependencies, and Galaxy info. |
| `module_utils/`   | ❌ | ✅ | ❌ | Shared Python utilities for modules. |
| `molecule/`       | ✅ | ❌ | ❌ | Molecule test scenarios for roles. |
| `playbooks/`      | ❌ | ✅ | ❌ | Standalone playbooks. |
| `plugins/`        | ❌ | ✅ | ❌ | Custom plugins (filters, lookups, callbacks, etc.). |
| `roles/`          | ❌ | ✅ | ❌ | Modular, reusable role definitions. |
| `tasks/`          | ✅ | ❌ | ❌ | Core task definitions for a role. |
| `templates/`      | ✅ | ✅ | ✅ | Jinja2 templates for dynamic file generation. |
| `tests/`          | ✅ | ✅ | ✅ | Test playbooks or validation scripts. |
| `vars/`           | ✅ | ✅ | ✅ | Higher-priority variables than defaults. |

## Common Sections in a Playbook

| **Section**     | **Purpose** | **Best Practice?** | **Extra Notes** |
|-----------------|-------------|--------------------|-----------------|
| `pre_tasks`     | Runs before roles and tasks. Often used for setup or checks. | ✅ Yes | Useful for environment validation, package cache refresh. |
| `tasks`         | Main execution block. | ✅ Required | Can include or import other task files. |
| `roles`         | Specifies which roles to run. | ✅ Yes | Encourages modular playbooks. |
| `post_tasks`    | Runs after roles and tasks. | ✅ Yes | Good for cleanup or reporting. |
| `handlers`      | Event-driven tasks triggered by changes. | ✅ Yes | Reduces unnecessary service restarts. |
| `vars`          | Playbook-level variables. | ✅ Yes | Best for small, playbook-specific settings. |
| `vars_files`    | External variable files. | ✅ Yes | Helps keep playbooks tidy. |
| `vars_prompt`   | Prompt for values during runtime. | ⚠️ Sparingly | Better to use `--extra-vars` for automation. |
| `tags`          | Filter tasks by label. | ✅ Yes | Improves speed and focus. |
| `ignore_errors` | Continue after task failure. | ⚠️ Carefully | Only when failure is non-critical. |

### Execution Flags & CLI Tips
```bash
--check                  # Dry-run mode to preview changes
--diff                   # Show changes to files/templates
--limit <host>           # Run playbook on a specific host or group
--tags <tag>             # Include tasks by tag
--skip-tags <tag>        # Exclude tasks by tag
--start-at-task "name"   # Resume from a specific task
-e key=value             # Pass extra variables
```

### Variable Precedence Overview (Lowest to Highest)

1. Role defaults (defaults/main.yml)
2. Inventory group_vars and host_vars
3. Playbook vars
4. Extra vars (-e on CLI)

### Useful Ansible Commands

```bash
ansible-inventory --list -y                # View inventory data
ansible-playbook --list-tags playbook.yml  # List available tags
ansible-playbook --list-tasks playbook.yml # List tasks without running them
ansible-galaxy install -r requirements.yml # Install role/collection dependencies
```

### Testing and Linting

```bash
ansible-lint        # Static analysis for best practices
molecule test       # Full role test cycle
molecule converge   # Apply role in a test environment
molecule verify     # Run verification tests after converge
```

### Best Practices Reminders

- Keep playbooks idempotent.
- Group related variables in logical files.
- Use handlers to optimize changes.
- Avoid hardcoding credentials—use Ansible Vault.
- Keep templates clean and minimal in logic.
- Commit requirements.yml instead of installed collections/roles.