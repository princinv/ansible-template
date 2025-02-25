# ==========================================
# ANSIBLE PLAYBOOK TEMPLATE
# ==========================================

# ------------------------------------------
# FOLDER STRUCTURE
# --
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

## SUBFOLDERS

### ROLES 


| Directory         | **Role-Level Only** | **Playbook-Level Only** | **Both** |
|------------------|------------------|------------------|------------------|
| `meta/`         | ✅ | ❌ | ❌ |
| `defaults/`     | ✅ | ❌ | ❌ |
| `tasks/`        | ✅ | ❌ | ❌ |
| `molecule/`     | ✅ | ❌ | ❌ |
| `inventory/`    | ❌ | ✅ | ❌ |
| `files/`        | ❌ | ✅ | ❌ |
| `plugins/`      | ❌ | ✅ | ❌ |
| `module_utils/` | ❌ | ✅ | ❌ |
| `playbooks/`    | ❌ | ✅ | ❌ |
| `roles/`        | ❌ | ✅ | ❌ |
| `library/`      | ✅ | ✅ | ✅ |
| `handlers/`     | ✅ | ✅ | ✅ |
| `templates/`    | ✅ | ✅ | ✅ |
| `tests/`        | ✅ | ✅ | ✅ |
| `vars/`         | ✅ | ✅ | ✅ |