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


class CallbackConfig(Model):
    """The configuration of service URI and custom headers for the webhook.

    :param service_uri: The service URI for the webhook to post notifications.
    :type service_uri: str
    :param custom_headers: Custom headers that will be added to the webhook
     notifications.
    :type custom_headers: dict[str, str]
    """

    _validation = {
        'service_uri': {'required': True},
    }

    _attribute_map = {
        'service_uri': {'key': 'serviceUri', 'type': 'str'},
        'custom_headers': {'key': 'customHeaders', 'type': '{str}'},
    }

    def __init__(self, service_uri, custom_headers=None):
        super(CallbackConfig, self).__init__()
        self.service_uri = service_uri
        self.custom_headers = custom_headers