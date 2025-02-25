# Custom Lookup Plugins

The `lookup_plugins/` folder contains **custom lookup functions** to retrieve data dynamically.

## Example: Custom Lookup Plugin
A simple lookup plugin: `lookup_plugins/custom_lookup.py`

```python
from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        return [term.upper() for term in terms]
```

## Usage in Playbooks:
```yaml
- debug:
    msg: "{{ lookup('custom_lookup', 'hello', 'world') }}"
```