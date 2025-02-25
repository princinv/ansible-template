# Ansible Filter Plugins Directory

## 📌 What is the `filter_plugins/` Directory?
The `filter_plugins/` directory in an Ansible project or role is used to store **custom Jinja2 filters** that extend Ansible's templating capabilities.

## 📦 Why Use the `filter_plugins/` Directory?
- 🛠 **Extends Jinja2 functionality** beyond built-in filters.
- 🔄 **Allows for reusable transformations** of data within playbooks and templates.
- 🚀 **Improves readability and efficiency** by keeping complex logic out of playbooks.

## 📄 How to Use the `filter_plugins/` Directory
### 🔹 Creating a Custom Filter
Each filter must be defined in a Python script inside `filter_plugins/`. 
Example: `filter_plugins/custom_filters.py`
```python
def uppercase(value):
    return value.upper()

class FilterModule(object):
    def filters(self):
        return {"uppercase": uppercase}
```

### 🔹 Using the Custom Filter in Playbooks
Once placed in `filter_plugins/`, the filter can be used in tasks:
```yaml
- name: Convert text to uppercase
  debug:
    msg: "{{ 'hello world' | uppercase }}"
```
✅ **Output:** `"HELLO WORLD"`

### 🔹 Using the Custom Filter in Templates
Filters can be applied in Jinja2 templates:
```jinja2
{{ some_variable | uppercase }}
```

## 🔍 How Ansible Loads Filters
Ansible automatically loads any Python files in `filter_plugins/` as long as the directory is at the **same level as the playbook or role**.

To verify loaded filters, use:
```bash
ansible-doc -t filter -l
```

## 🏆 Best Practices
- **Keep filter names unique** to avoid conflicts with built-in Ansible filters.
- **Use descriptive function names** for clarity (e.g., `convert_to_json`, `strip_whitespace`).
- **Test filters separately** before using them in playbooks.
- **Avoid excessive complexity**—keep functions simple and focused.

The `filter_plugins/` directory enables powerful, reusable Jinja2 transformations within Ansible workflows, making playbooks and templates more dynamic and efficient.

