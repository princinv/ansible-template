  __much thanks to (@geerlingguy)[https://github.com/geerlingguy] for the great materials on using ansible.__

**WIP**

A complete template of default digestible directory structures in Ansible playbook. 

With some customizations. 

## RESOURCES



## FOLDER STRUCTURE

```markdown
playbook-template/
├── collections/                 # Custom collections (if needed)
├── files/                       # Static files (configs, certs, etc.)
├── handlers/                    # Handlers for global tasks
├── inventory/                   # Hosts and variable files
    ├── hosts.yml                # Inventory definition
    ├── group_vars/              # Variables per group (auto-loaded)
    │   ├── all.yml              # Loaded for all hosts
    │   ├── proxmox.yml          # Specific to "proxmox" group
    ├── host_vars/               # Variables per host (auto-loaded)
    │   ├── hl-core-ubuntu.yml   # Variables for a specific host
├── library/                     # Custom Ansible modules
├── module_utils/                # Shared utilities for custom modules
├── plugins/                     # Custom plugins
    ├── callback_plugins/        # Custom lookup plugins
    ├── filter_plugins/          # Custom Jinja2 filters
    ├── lookup_plugins/          # Custom lookup plugins
├── playbooks/                   # Standalone playbooks
├── roles/                       # Role definitions (modular configurations)
└── role_name/
    ├── tasks/                   # REQUIRED: Main role logic (main.yml auto-loaded)
    │   ├── main.yml             # Auto-loaded when role is applied
    ├── handlers/                # Handlers for restarting services
    │   ├── main.yml             # Auto-loaded when role needs handlers
    ├── templates/               # Jinja2 templates (.j2) for config files
    ├── files/                   # Static files to be copied
    ├── vars/                    # Role-specific variables (auto-loaded)
    │   ├── main.yml             # Automatically included variables
    ├── defaults/                # Default variables (lowest priority)
    │   ├── main.yml             # Lowest priority variables (overridable)
    ├── meta/                    # Metadata (dependencies, author, etc.)
    │   ├── main.yml             # Automatically run tasks
    ├── library/                 # Custom modules **(same as top-level)**
    ├── tests/                   # Playbook tests for the role
    │   ├── test.yml             # Sample test playbook for the role
    ├── molecule/                # Molecule testing framework
    │   ├── default/             # Default test scenario
    │   │   ├── molecule.yml     # Molecule configuration file
    │   │   ├── playbook.yml     # Test playbook for the role
    │   │   ├── tests/           # Test assertions 
    |   |       |──testinfra.py  # validation, post-deployment verification, ensure system state is correct
├── templates/                   # Jinja2 templates
├── tests/                       # Playbook tests
├── vars/                        # Global variable files
├── ansible.cfg                  # Configuration settings
├── bootstrap.sh                 # Ensure environment is ready
├── requirements.yml             # Ansible Galaxy role dependencies
├── requirements.txt             # Python dependencies
```


## Directory Information

| Directory         | **Role-Level Only** | **Playbook-Level Only** | **Both** |
|------------------|------------------|------------------|------------------|
| `collections/`   | ❌ | ✅ | ❌ |
| `defaults/`     | ✅ | ❌ | ❌ |
| `files/`        | ❌ | ✅ | ❌ |
| `handlers/`     | ✅ | ✅ | ✅ |
| `inventory/`    | ❌ | ✅ | ❌ |
| `library/`      | ✅ | ✅ | ✅ |
| `meta/`         | ✅ | ❌ | ❌ |
| `module_utils/` | ❌ | ✅ | ❌ |
| `molecule/`     | ✅ | ❌ | ❌ |
| `playbooks/`    | ❌ | ✅ | ❌ |
| `plugins/`      | ❌ | ✅ | ❌ |
| `roles/`        | ❌ | ✅ | ❌ |
| `tasks/`        | ✅ | ❌ | ❌ |
| `templates/`    | ✅ | ✅ | ✅ |
| `tests/`        | ✅ | ✅ | ✅ |
| `vars/`         | ✅ | ✅ | ✅ |


## Common Sections in a Playbook

| **Section** | **Purpose** | **Best Practice?** |
|------------|------------|----------------|
| `pre_tasks` | Runs **before roles and tasks** (e.g., checking dependencies, setting up environment variables). | ✅ **Yes**, if setup tasks are required before roles. |
| `tasks` | The **main execution block** where all playbook actions happen. | ✅ **Required** (unless using roles exclusively). |
| `roles` | Defines **which roles to apply** to hosts. | ✅ **Yes**, if using roles for modularity. |
| `post_tasks` | Runs **after roles and tasks** (e.g., final cleanup or notifications). | ✅ **Yes**, if post-processing is needed. |
| `handlers` | Defines **event-driven tasks** (e.g., restart services only if a change occurs). | ✅ **Yes**, for efficient playbooks. |
| `vars` | Defines **variables specific to this playbook**. | ✅ **Yes**, if playbook-specific variables are needed. |
| `vars_files` | Loads **external variable files** into the playbook. | ✅ **Yes**, if variables are stored externally. |
| `vars_prompt` | Prompts the user to enter variables interactively. | ⚠️ **Use Sparingly**, better to use `--extra-vars`. |
| `tags` | Allows **running only specific tasks** in the playbook. | ✅ **Yes**, improves task targeting. |
| `ignore_errors` | Lets the playbook **continue running even if a task fails**. | ⚠️ **Use Carefully**, can hide failures. |
