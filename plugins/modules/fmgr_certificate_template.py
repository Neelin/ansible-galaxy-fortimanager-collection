#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2020 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fmgr_certificate_template
short_description: no description
description:
    - This module is able to configure a FortiManager device.
    - Examples include all parameters and values which need to be adjusted to data sources before usage.

version_added: "2.10"
author:
    - Link Zheng (@chillancezen)
    - Jie Xue (@JieX19)
    - Frank Shen (@fshen01)
    - Hongbin Lu (@fgtdev-hblu)
notes:
    - Running in workspace locking mode is supported in this FortiManager module, the top
      level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
    - To create or update an object, use state present directive.
    - To delete an object, use state absent directive.
    - Normally, running one module can fail when a non-zero rc is returned. you can also override
      the conditions to fail or succeed with parameters rc_failed and rc_succeeded

options:
    bypass_validation:
        description: only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters
        required: false
        type: bool
        default: false
    workspace_locking_adom:
        description: the adom to lock for FortiManager running in workspace mode, the value can be global and others including root
        required: false
        type: str
    workspace_locking_timeout:
        description: the maximum time in seconds to wait for other user to release the workspace lock
        required: false
        type: int
        default: 300
    state:
        description: the directive to create, update or delete an object
        type: str
        required: true
        choices:
          - present
          - absent
    rc_succeeded:
        description: the rc codes list with which the conditions to succeed will be overriden
        type: list
        required: false
    rc_failed:
        description: the rc codes list with which the conditions to fail will be overriden
        type: list
        required: false
    adom:
        description: the parameter (adom) in requested url
        type: str
        required: true
    certificate_template:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            city:
                type: str
                description: no description
            country:
                type: str
                description: no description
            digest-type:
                type: str
                default: 'sha1'
                description: no description
                choices:
                    - 'sha1'
                    - 'sha256'
            email:
                type: str
                description: no description
            id-type:
                type: str
                default: 'host-ip'
                description: no description
                choices:
                    - 'host-ip'
                    - 'domain-name'
                    - 'email'
            key-size:
                type: str
                default: '2048'
                description: no description
                choices:
                    - '512'
                    - '1024'
                    - '1536'
                    - '2048'
            key-type:
                type: str
                default: 'rsa'
                description: no description
                choices:
                    - 'rsa'
            name:
                type: str
                description: no description
            organization:
                type: str
                description: no description
            organization-unit:
                description: no description
                type: str
            scep-password:
                description: no description
                type: str
            scep-server:
                type: str
                description: no description
            state:
                type: str
                description: no description
            subject-name:
                type: str
                description: no description
            type:
                type: str
                default: 'external'
                description: no description
                choices:
                    - 'external'
                    - 'local'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: no description
      fmgr_certificate_template:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         certificate_template:
            city: <value of string>
            country: <value of string>
            digest-type: <value in [sha1, sha256]>
            email: <value of string>
            id-type: <value in [host-ip, domain-name, email]>
            key-size: <value in [512, 1024, 1536, ...]>
            key-type: <value in [rsa]>
            name: <value of string>
            organization: <value of string>
            organization-unit: <value of string>
            scep-password: <value of string>
            scep-server: <value of string>
            state: <value of string>
            subject-name: <value of string>
            type: <value in [external, local]>

'''

RETURN = '''
request_url:
    description: The full url requested
    returned: always
    type: str
    sample: /sys/login/user
response_code:
    description: The status of api request
    returned: always
    type: int
    sample: 0
response_message:
    description: The descriptive message of the api response
    type: str
    returned: always
    sample: OK.

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortimanager.plugins.module_utils.NAPI import NAPIManager
from ansible_collections.fortinet.fortimanager.plugins.module_utils.NAPI import check_galaxy_version
from ansible_collections.fortinet.fortimanager.plugins.module_utils.NAPI import check_parameter_bypass


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/certificate/template',
        '/pm/config/global/obj/certificate/template'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/certificate/template/{template}',
        '/pm/config/global/obj/certificate/template/{template}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'bypass_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'workspace_locking_adom': {
            'type': 'str',
            'required': False
        },
        'workspace_locking_timeout': {
            'type': 'int',
            'required': False,
            'default': 300
        },
        'rc_succeeded': {
            'required': False,
            'type': 'list'
        },
        'rc_failed': {
            'required': False,
            'type': 'list'
        },
        'state': {
            'type': 'str',
            'required': True,
            'choices': [
                'present',
                'absent'
            ]
        },
        'adom': {
            'required': True,
            'type': 'str'
        },
        'certificate_template': {
            'required': False,
            'type': 'dict',
            'options': {
                'city': {
                    'required': False,
                    'type': 'str'
                },
                'country': {
                    'required': False,
                    'type': 'str'
                },
                'digest-type': {
                    'required': False,
                    'choices': [
                        'sha1',
                        'sha256'
                    ],
                    'default': 'sha1',
                    'type': 'str'
                },
                'email': {
                    'required': False,
                    'type': 'str'
                },
                'id-type': {
                    'required': False,
                    'choices': [
                        'host-ip',
                        'domain-name',
                        'email'
                    ],
                    'default': 'host-ip',
                    'type': 'str'
                },
                'key-size': {
                    'required': False,
                    'choices': [
                        '512',
                        '1024',
                        '1536',
                        '2048'
                    ],
                    'default': '2048',
                    'type': 'str'
                },
                'key-type': {
                    'required': False,
                    'choices': [
                        'rsa'
                    ],
                    'default': 'rsa',
                    'type': 'str'
                },
                'name': {
                    'required': True,
                    'type': 'str'
                },
                'organization': {
                    'required': False,
                    'type': 'str'
                },
                'organization-unit': {
                    'required': False,
                    'type': 'str'
                },
                'scep-password': {
                    'required': False,
                    'type': 'str'
                },
                'scep-server': {
                    'required': False,
                    'type': 'str'
                },
                'state': {
                    'required': False,
                    'type': 'str'
                },
                'subject-name': {
                    'required': False,
                    'type': 'str'
                },
                'type': {
                    'required': False,
                    'choices': [
                        'external',
                        'local'
                    ],
                    'default': 'external',
                    'type': 'str'
                }
            }

        }
    }

    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'certificate_template'),
                           supports_check_mode=False)

    fmgr = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        fmgr = NAPIManager(jrpc_urls, perobject_jrpc_urls, module_primary_key, url_params, module, connection, top_level_schema_name='data')
        fmgr.process_curd()
    else:
        module.fail_json(msg='MUST RUN IN HTTPAPI MODE')
    module.exit_json(meta=module.params)


if __name__ == '__main__':
    main()