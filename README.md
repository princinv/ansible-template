# README.md
# ==========================================
# ANSIBLE PLAYBOOK TEMPLATE
# ==========================================

# ------------------------------------------
# FOLDER STRUCTURES
# --

## TOP LEVEL

ansible-homelab/
├── inventory/        # Hosts and variable files
├── roles/            # Role definitions (modular configurations)
├── playbooks/        # Standalone playbooks
├── collections/      # Custom collections (if needed)
├── plugins/          # Custom plugins
├── library/          # Custom Ansible modules
├── filter_plugins/   # Custom Jinja2 filters
├── lookup_plugins/   # Custom lookup plugins
├── module_utils/     # Shared utilities for custom modules
├── vars/             # Global variable files
├── files/            # Static files (configs, certs, etc.)
├── templates/        # Jinja2 templates
├── handlers/         # Handlers for global tasks
├── tests/            # Playbook tests
├── ansible.cfg       # Configuration settings
├── requirements.yml  # Ansible Galaxy role dependencies
├── README.md         # Documentation

## SUBFOLDERS

### ROLES 

roles/
└── role_name/
    ├── tasks/             # REQUIRED: Main role logic (main.yml auto-loaded)
    │   ├── main.yml       # Auto-loaded when role is applied
    ├── handlers/          # Handlers for restarting services
    │   ├── main.yml       # Auto-loaded when role needs handlers
    ├── templates/         # Jinja2 templates (.j2) for config files
    ├── files/             # Static files to be copied
    ├── vars/              # Role-specific variables (auto-loaded)
    │   ├── main.yml       # Automatically included variables
    ├── defaults/          # Default variables (lowest priority)
    │   ├── main.yml       # Lowest priority variables (overridable)
    ├── meta/              # Metadata (dependencies, author, etc.)
    │   ├── main.yml       
    ├── library/           # Custom modules **(same as top-level)**
    ├── module_utils/      # Custom utilities for modules **(same as top-level)**
    ├── filter_plugins/    # Custom Jinja2 filters **(same as top-level)**
    ├── lookup_plugins/    # Custom lookup functions **(same as top-level)**
    ├── tests/             # Playbook tests for the role
    │   ├── test.yml       # Sample test playbook for the role
    ├── README.md          # Optional but good for documentation



### INVENTORY

inventory/
├── hosts.yml            # Inventory definition
├── group_vars/          # Variables per group (auto-loaded)
│   ├── all.yml          # Loaded for all hosts
│   ├── proxmox.yml      # Specific to "proxmox" group
├── host_vars/           # Variables per host (auto-loaded)
│   ├── hl-core-ubuntu.yml   # Variables for a specific host


