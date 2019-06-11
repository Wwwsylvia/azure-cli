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


class SetValue(Model):
    """The properties of a overridable value that can be passed to a task
    template.

    :param name: The name of the overridable value.
    :type name: str
    :param value: The overridable value.
    :type value: str
    :param is_secret: Flag to indicate whether the value represents a secret
     or not. Default value: False .
    :type is_secret: bool
    """

    _validation = {
        'name': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'is_secret': {'key': 'isSecret', 'type': 'bool'},
    }

    def __init__(self, name, value, is_secret=False):
        super(SetValue, self).__init__()
        self.name = name
        self.value = value
        self.is_secret = is_secret