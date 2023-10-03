
---
<img src="Netology.png" height="24px"/>

### Учебная группа DevOps-32

---

## Решение по домашнему заданию к занятию 6 «Создание собственных модулей»


- [Описание](#description)
- [Требования к инфраструктуре](#requirements)
- [Переменные и настройки](#vars-and-setup)
- [Запуск](#play)
- [Исполнитель](#student)

---

###### Description
### Описание

Здесь приводится результат выполнения домашнего задания 6 «Создание собственных модулей» для Ansible.

В этом репозитории содержится Ansible collection, содержащая написанный в рамках обучения тестовый модуль `beatl_module`.

Также collection включает в себя Ansible role `module_test` использующую тестовый модуль и расположенный в корневой директории single task playbook `site.yml`, показывающий использование role.

---

###### Requirements
### Требования к инфрастуктуре

Для успешного запуска требуется:

1. Python 3.10
2. Ansible [core 2.15.3]

---

###### Vars and Setup
### Переменные и настройки

--------------
| Variable  |      |
|:-----|:----|
| file_path | Path to file to be created on managed node, include file name |
| file_content  | Content of the file to be written |


---

###### Play
### Запуск

В рамках изучения написания модуля для Ansible приведены несколько способов запуска.

Проверка самого модуля реализованного на Python:

``` 
python3 beatl_module.py pl.json
```

<details>
    <summary> Вывод Python...  </summary>

```
(venv) beatl@OWEN:~/arep/ansible$ python3 beatl_module.py pl.json
{"changed": true, "failed": false, "original_message": "testfile.txt", "message": "File: testfile.txt contains Ansible is the best...", "invocation": {"module_args": {"new_path": "testfile.txt", "content": "Ansible is the best..."}}}
```

</details>

---

Проверка модуля с помощью Ansible single task playbook:

```
ansible-playbook site.yml
```

playbook запускается дважды для проверки на идемпотентность.

<details>
    <summary> Вывод Ansible ...  </summary>

```
(venv) beatl@OWEN:~/arep/ansible$ ansible-playbook site.yml
[WARNING]: You are running the development version of Ansible. You should only
run Ansible from "devel" if you are modifying the Ansible engine, or trying out
features under development. This is a rapidly changing source of code and can
become unstable at any point.
[WARNING]: provided hosts list is empty, only localhost is available. Note that
the implicit localhost does not match 'all'

PLAY [Test my module] **********************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Call my test_module] *****************************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

(venv) beatl@OWEN:~/arep/ansible$ ansible-playbook site.yml
[WARNING]: You are running the development version of Ansible. You should only
run Ansible from "devel" if you are modifying the Ansible engine, or trying out
features under development. This is a rapidly changing source of code and can
become unstable at any point.
[WARNING]: provided hosts list is empty, only localhost is available. Note that
the implicit localhost does not match 'all'

PLAY [Test my module] **********************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Call my test_module] *****************************************************
ok: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

</details>

---

Проверка после распаковки из архива:

```
ansible-galaxy collection install beatljs-yandex_cloud_elk-1.0.0.tar.gz
```

<details>
    <summary> Вывод bash...  </summary>

```
beatl@OWEN:~/collection_from_arch$ ls
beatljs-yandex_cloud_elk-1.0.0.tar.gz
beatl@OWEN:~/collection_from_arch$ ansible-galaxy collection install beatljs-yandex_cloud_elk-1.0.0.tar.gz
Starting galaxy collection install process
Process install dependency map
Starting collection install process
Installing 'beatljs.yandex_cloud_elk:1.0.0' to '/home/beatl/.ansible/collections/ansible_collections/beatljs/yandex_cloud_elk'
beatljs.yandex_cloud_elk:1.0.0 was installed successfully
```

</details>

```
ansible-playbook site.yml
```

<details>
    <summary> Вывод Ansible...  </summary>

```
beatl@OWEN:~/collection_from_arch$ ansible-playbook site.yml
[WARNING]: provided hosts list is empty, only localhost is available. Note that
the implicit localhost does not match 'all'

PLAY [Test my module] **********************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [module_test : Call my test_module] ***************************************
ok: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
</details>


---

###### Student
### Исполнитель

Сергей Жуков DevOps-32

---


