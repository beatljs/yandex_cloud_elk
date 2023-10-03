#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: beatl_module

short_description: This is my test module

description: This is my longer description explaining my test module.
             Module create file with content passed in "content" parameter.
             File path and file name passed in "new_path" parameter.
options:
    new_path:
        description:
            - This is the path to send to the test module. Must contain path to file and file name
        required: true
        type: str
    content:
        description:
            - String to be as content in created file.
        required: false
        type: str
        default: 'Ansible is the best...'

extends_documentation_fragment:
    - beatljs.beatl_collection.my_doc_fragment_name

author:
    - Sergey Zhukov (@beatljs)
'''

EXAMPLES = r'''
# Pass in a message. If file passed in new_path not exist, changed set true.
- new_path: Path to file to be created include file name
  beatljs.beatl_collection.my_test:
    new_path: '/temp/my_file.txt'

# pass in a message and replace default content with new
- name: Test with a message and changed output
  beatljs.beatl_collection.my_test:
    new_path: '/temp/my_file.txt'
    content: 'any string blablabla'

# fail the module
- name: Test failure of the module
  beatljs.beatl_collection.my_test:
    new_path: wrong path string (e.g. '\,qwu=-/file.txt')
'''

RETURN = r'''
original_message:
    description: The original new_path param that was passed in.
    type: str
    returned: always
    sample: '/temp/my_file.txt'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'File: my_file.txt contains Ansible is the best...'
'''

import os.path
from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        new_path=dict(type='str', required=True),
        content=dict(type='str', required=False, default='Ansible is the best...')
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        failed=False,
        original_message='',
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    result['original_message'] = module.params['new_path']
    result['message'] = 'File: {} contains {}'.format(module.params['new_path'],module.params['content'])

    if os.path.isfile(module.params['new_path'])==False:
      result['changed']=True

    # !!! тут надо бы еще проверку на содержимое сделать, но в рамках изучения модулей Ansible - это непринципиально.

    try:
      with open(module.params['new_path'], "w+") as my_file:
        my_file.write(module.params['content'])
        my_file.close()
    except OSError:
      module.fail_json(msg='ERR: File creation error ...', **result)


    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()

