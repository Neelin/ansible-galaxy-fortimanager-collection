#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2021 Fortinet, Inc.
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
module: fmgr_devprof_system_emailserver
short_description: Configure the email server used by the FortiGate various things.
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
    enable_log:
        description: Enable/Disable logging for task
        required: false
        type: bool
        default: false
    proposed_method:
        description: The overridden method for the underlying Json RPC request
        required: false
        type: str
        choices:
          - update
          - set
          - add
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
    devprof:
        description: the parameter (devprof) in requested url
        type: str
        required: true
    devprof_system_emailserver:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            authenticate:
                type: str
                description: 'Enable/disable authentication.'
                choices:
                    - 'disable'
                    - 'enable'
            password:
                description: no description
                type: str
            port:
                type: int
                description: 'SMTP server port.'
            reply-to:
                type: str
                description: 'Reply-To email address.'
            security:
                type: str
                description: 'Connection security used by the email server.'
                choices:
                    - 'none'
                    - 'starttls'
                    - 'smtps'
            server:
                type: str
                description: 'SMTP server IP address or hostname.'
            source-ip:
                type: str
                description: 'SMTP server IPv4 source IP.'
            source-ip6:
                type: str
                description: 'SMTP server IPv6 source IP.'
            ssl-min-proto-version:
                type: str
                description: 'Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).'
                choices:
                    - 'default'
                    - 'TLSv1'
                    - 'TLSv1-1'
                    - 'TLSv1-2'
                    - 'SSLv3'
            type:
                type: str
                description: 'Use FortiGuard Message service or custom email server.'
                choices:
                    - 'custom'
            username:
                type: str
                description: 'SMTP server user name for authentication.'
            validate-server:
                type: str
                description: 'Enable/disable validation of server certificate.'
                choices:
                    - 'disable'
                    - 'enable'
            interface:
                type: str
                description: 'Specify outgoing interface to reach server.'
            interface-select-method:
                type: str
                description: 'Specify how to select outgoing interface to reach server.'
                choices:
                    - 'auto'
                    - 'sdwan'
                    - 'specify'

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
    - name: Configure the email server used by the FortiGate various things.
      fmgr_devprof_system_emailserver:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         devprof: <your own value>
         devprof_system_emailserver:
            authenticate: <value in [disable, enable]>
            password: <value of string>
            port: <value of integer>
            reply-to: <value of string>
            security: <value in [none, starttls, smtps]>
            server: <value of string>
            source-ip: <value of string>
            source-ip6: <value of string>
            ssl-min-proto-version: <value in [default, TLSv1, TLSv1-1, ...]>
            type: <value in [custom]>
            username: <value of string>
            validate-server: <value in [disable, enable]>
            interface: <value of string>
            interface-select-method: <value in [auto, sdwan, specify]>

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
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import NAPIManager
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import check_galaxy_version
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import check_parameter_bypass


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/devprof/{devprof}/system/email-server'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/devprof/{devprof}/system/email-server/{email-server}'
    ]

    url_params = ['adom', 'devprof']
    module_primary_key = None
    module_arg_spec = {
        'enable_log': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'proposed_method': {
            'type': 'str',
            'required': False,
            'choices': [
                'set',
                'update',
                'add'
            ]
        },
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
        'adom': {
            'required': True,
            'type': 'str'
        },
        'devprof': {
            'required': True,
            'type': 'str'
        },
        'devprof_system_emailserver': {
            'required': False,
            'type': 'dict',
            'revision': {
                '6.0.0': True,
                '6.2.1': True,
                '6.2.3': True,
                '6.2.5': True,
                '6.4.0': True,
                '6.4.5': True,
                '7.0.0': True
            },
            'options': {
                'authenticate': {
                    'required': False,
                    'revision': {
                        '6.0.0': True,
                        '6.2.1': True,
                        '6.2.3': True,
                        '6.2.5': True,
                        '6.4.0': True,
                        '6.4.2': False,
                        '6.4.5': True,
                        '7.0.0': True
                    },
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'password': {
                    'required': False,
                    'revision': {
                        '6.0.0': True,
                        '6.2.1': True,
                        '6.2.3': True,
                        '6.2.5': True,
                        '6.4.0': True,
                        '6.4.2': False,
                        '6.4.5': True,
                        '7.0.0': True
                    },
                    'type': 'str'
                },
                'port': {
                    'required': False,
                    'revision': {
                        '6.0.0': True,
                        '6.2.1': True,
                        '6.2.3': True,
                        '6.2.5': True,
                        '6.4.0': True,
                        '6.4.2': False,
                        '6.4.5': True,
                        '7.0.0': True
                    },
                    'type': 'int'
                },
                'reply-to': {
                    'required': False,
                    'revision': {
                        '6.0.0': True,
                        '6.2.1': True,
                        '6.2.3': True,
                        '6.2.5': True,
                        '6.4.0': True,
                        '6.4.2': False,
                        '6.4.5': True,
                        '7.0.0': True
                    },
                    'type': 'str'
                },
                'security': {
                    'required': False,
                    'revision': {
                        '6.0.0': True,
                        '6.2.1': True,
                        '6.2.3': True,
                        '6.2.5': True,
                        '6.4.0': True,
                        '6.4.2': False,
                        '6.4.5': True,
                        '7.0.0': True
                    },
                    'choices': [
                        'none',
                        'starttls',
                        'smtps'
                    ],
                    'type': 'str'
                },
                'server': {
                    'required': False,
                    'revision': {
                        '6.0.0': True,
                        '6.2.1': True,
                        '6.2.3': True,
                        '6.2.5': True,
                        '6.4.0': True,
                        '6.4.2': False,
                        '6.4.5': True,
                        '7.0.0': True
                    },
                    'type': 'str'
                },
                'source-ip': {
                    'required': False,
                    'revision': {
                        '6.0.0': True,
                        '6.2.1': True,
                        '6.2.3': True,
                        '6.2.5': True,
                        '6.4.0': True,
                        '6.4.2': False,
                        '6.4.5': True,
                        '7.0.0': True
                    },
                    'type': 'str'
                },
                'source-ip6': {
                    'required': False,
                    'revision': {
                        '6.0.0': True,
                        '6.2.1': True,
                        '6.2.3': True,
                        '6.2.5': True,
                        '6.4.0': True,
                        '6.4.2': False,
                        '6.4.5': True,
                        '7.0.0': True
                    },
                    'type': 'str'
                },
                'ssl-min-proto-version': {
                    'required': False,
                    'revision': {
                        '6.0.0': True,
                        '6.2.1': True,
                        '6.2.3': True,
                        '6.2.5': True,
                        '6.4.0': True,
                        '6.4.2': False,
                        '6.4.5': True,
                        '7.0.0': True
                    },
                    'choices': [
                        'default',
                        'TLSv1',
                        'TLSv1-1',
                        'TLSv1-2',
                        'SSLv3'
                    ],
                    'type': 'str'
                },
                'type': {
                    'required': False,
                    'revision': {
                        '6.0.0': True,
                        '6.2.1': True,
                        '6.2.3': True,
                        '6.2.5': True,
                        '6.4.0': True,
                        '6.4.2': False,
                        '6.4.5': True,
                        '7.0.0': True
                    },
                    'choices': [
                        'custom'
                    ],
                    'type': 'str'
                },
                'username': {
                    'required': False,
                    'revision': {
                        '6.0.0': True,
                        '6.2.1': True,
                        '6.2.3': True,
                        '6.2.5': True,
                        '6.4.0': True,
                        '6.4.2': False,
                        '6.4.5': True,
                        '7.0.0': True
                    },
                    'type': 'str'
                },
                'validate-server': {
                    'required': False,
                    'revision': {
                        '6.0.0': True,
                        '6.2.1': True,
                        '6.2.3': True,
                        '6.2.5': True,
                        '6.4.0': True,
                        '6.4.2': False,
                        '6.4.5': True,
                        '7.0.0': True
                    },
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'interface': {
                    'required': False,
                    'revision': {
                        '7.0.0': True
                    },
                    'type': 'str'
                },
                'interface-select-method': {
                    'required': False,
                    'revision': {
                        '7.0.0': True
                    },
                    'choices': [
                        'auto',
                        'sdwan',
                        'specify'
                    ],
                    'type': 'str'
                }
            }

        }
    }

    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'devprof_system_emailserver'),
                           supports_check_mode=False)

    fmgr = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        connection.set_option('enable_log', module.params['enable_log'] if 'enable_log' in module.params else False)
        fmgr = NAPIManager(jrpc_urls, perobject_jrpc_urls, module_primary_key, url_params, module, connection, top_level_schema_name='data')
        fmgr.validate_parameters(params_validation_blob)
        fmgr.process_partial_curd(argument_specs=module_arg_spec)
    else:
        module.fail_json(msg='MUST RUN IN HTTPAPI MODE')
    module.exit_json(meta=module.params)


if __name__ == '__main__':
    main()
