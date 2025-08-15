# plugins/filter_plugins/filters.py

# ==========================================
# CUSTOM FILTER PLUGINS
# ==========================================
# This module defines custom Jinja2 filter plugins for Ansible.
# Filters:
#   - bool_str: Convert a value to a lowercase "true"/"false" string.
#   - dict_merge: Merge two dictionaries into a new one.
#

def _bool_str(val):
    """
    Convert a value to a lowercase 'true' or 'false' string.
    Accepts truthy values: 1, 'true', 'yes', 'on'.
    """
    return "true" if str(val).lower() in ("1", "true", "yes", "on") else "false"


def _dict_merge(a, b):
    """
    Merge two dictionaries into a new one.
    Values from b will overwrite those from a.
    """
    out = dict(a or {})
    out.update(b or {})
    return out


class FilterModule(object):
    """Custom Ansible filters."""

    def filters(self):
        return {
            "bool_str": _bool_str,      # {{ myvar | bool_str }}
            "dict_merge": _dict_merge,  # {{ a | dict_merge(b) }}
        }
