## Default Ansible Variables


### Hosts & Users

| **Variable** | **Description** |
|-------------|----------------|
| `ansible_host` | The target host’s IP or hostname from inventory. |
| `ansible_hostname` | The short hostname of the target machine. |
| `ansible_nodename` | The system's hostname as returned by `uname -n`. |
| `inventory_hostname` | The name of the host as defined in the inventory. |
| `inventory_hostname_short` | The short version of `inventory_hostname`. |
| `ansible_fqdn` | The fully qualified domain name of the target. |
| `ansible_domain` | The domain name of the target machine. |
| `ansible_env` | A dictionary of environment variables from the remote host. |
| `ansible_user` | The remote user running the Ansible tasks. |
| `ansible_uid` | The UID of `ansible_user`. |
| `ansible_gid` | The GID of `ansible_user`. |
| `group_names` | List of all groups the host belongs to. |
| `ansible_play_hosts` | A list of hosts in the current play. |
| `ansible_play_batch` | The list of active hosts in the current batch. |


### Play Information

| **Variable** | **Description** |
|-------------|----------------|
| `ansible_date_time` | A dictionary containing the current date and time on the remote host. |
| `ansible_date_time.iso8601` | The current date/time in ISO8601 format. |
| `ansible_playbook_python` | The path to the Python interpreter running the playbook. |
| `ansible_version.full` | The full version of Ansible being used. |
| `ansible_version.major` | The major version number of Ansible. |
| `ansible_version.minor` | The minor version number of Ansible. |
| `ansible_version.revision` | The revision number of Ansible. |
| `ansible_connection` | The connection type (e.g., SSH, local). |
| `ansible_ssh_host` | The SSH hostname used for the connection. |
| `ansible_ssh_port` | The SSH port number. |
| `ansible_ssh_user` | The SSH username used for the connection. |


### Network Info

| **Variable** | **Description** |
|-------------|----------------|
| `ansible_default_ipv4.address` | The default IPv4 address of the machine. |
| `ansible_default_ipv6.address` | The default IPv6 address of the machine. |
| `ansible_interfaces` | A list of network interfaces on the target. |


### Hardware Info

| **Variable** | **Description** |
|-------------|----------------|
| `ansible_memtotal_mb` | Total system memory in MB. |
| `ansible_memfree_mb` | Available free memory in MB. |
| `ansible_swapfree_mb` | Amount of free swap space in MB. |
| `ansible_swaptotal_mb` | Total amount of swap space in MB. |
| `ansible_processor` | A list containing CPU model details. |
| `ansible_processor_count` | Number of physical processor cores. |
| `ansible_processor_vcpus` | Number of virtual CPUs. |
| `ansible_processor_cores` | The number of cores per processor socket. |
| `ansible_processor_threads_per_core` | The number of threads per processor core. |
| `ansible_disk_free` | The available disk space on the root filesystem. |
| `ansible_disk_total` | The total disk space on the root filesystem. |
| `ansible_uptime_seconds` | The system uptime in seconds. |
| `ansible_mounts` | A list of mounted filesystems and their properties. |
| `ansible_devices` | A dictionary of block storage devices on the system. |


### OS Info

| **Variable** | **Description** |
|-------------|----------------|
| `ansible_system` | The operating system family (e.g., `Linux`, `Windows`). |
| `ansible_machine` | The hardware architecture (e.g., `x86_64`, `arm`). |
| `ansible_product_uuid` | The system's hardware UUID. |
| `ansible_fips` | Boolean indicating if FIPS mode is enabled. |
| `ansible_form_factor` | The form factor of the remote system (e.g., `Laptop`, `Desktop`). |
| `ansible_bios_version` | The BIOS version of the remote system. |
| `ansible_bios_date` | The release date of the system BIOS. |
| `ansible_architecture` | The CPU architecture of the target system. |
| `ansible_kernel` | The kernel version of the OS. |
| `ansible_distribution` | The OS distribution (e.g., Ubuntu, CentOS). |
| `ansible_distribution_version` | The version of the OS. |
| `ansible_distribution_major_version` | The major version of the OS. |
| `ansible_lsb.id` | The Linux Standard Base distribution ID. |
| `ansible_lsb.release` | The LSB release version of the OS. |
| `ansible_lsb.codename` | The codename of the OS release. |
| `ansible_cmdline` | Kernel command-line arguments from `/proc/cmdline`. |
| `ansible_virtualization_role` | Whether the system is a guest or host in a virtualized environment. |
| `ansible_virtualization_type` | The type of virtualization detected (e.g., `kvm`, `vmware`, `docker`). |


### Misc

| **Variable** | **Description** |
|-------------|----------------|
| `ansible_user_shell` | The default shell for the Ansible remote user. |
| `ansible_pkg_mgr` | The package manager used by the target system (e.g., `apt`, `yum`). |
| `ansible_service_mgr` | The service manager used by the system (`systemd`, `init`). |
| `ansible_apparmor` | A dictionary containing AppArmor status and settings. |
| `ansible_selinux` | A dictionary containing SELinux mode and policy information. |
| `ansible_local` | A dictionary of locally-defined facts from `/etc/ansible/facts.d`. |




These built-in variables are automatically available in any playbook and can be referenced without needing to define them explicitly.
