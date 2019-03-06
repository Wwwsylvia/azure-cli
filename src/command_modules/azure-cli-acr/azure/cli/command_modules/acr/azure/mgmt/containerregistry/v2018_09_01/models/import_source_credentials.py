# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ImportSourceCredentials(Model):
    """ImportSourceCredentials.

    :param username: The username to authenticate with the source registry.
    :type username: str
    :param password: The password used to authenticate with the source
     registry.
    :type password: str
    """

    _validation = {
        'password': {'required': True},
    }

    _attribute_map = {
        'username': {'key': 'username', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
    }

    def __init__(self, password, username=None):
        super(ImportSourceCredentials, self).__init__()
        self.username = username
        self.password = password
