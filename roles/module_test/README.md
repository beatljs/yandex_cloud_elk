Module_test
=========

This training role for testing module `beatl_module`

Role Variables
--------------
| Variable  |      |
|:-----|:----|
| file_path | Path to file to be created on managed node include file name |
| file_content  | Content of the file to be written |

Example Playbook
----------------

```yml
    - name: Test beatl_module
      hosts: localhost
      roles:
        - module_test
```

