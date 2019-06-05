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


class SourceTrigger(Model):
    """The properties of a source based trigger.

    :param source_repository: The properties that describes the source(code)
     for the task.
    :type source_repository:
     ~azure.mgmt.containerregistry.v2019_04_01.models.SourceProperties
    :param source_trigger_events: The source event corresponding to the
     trigger.
    :type source_trigger_events: list[str or
     ~azure.mgmt.containerregistry.v2019_04_01.models.SourceTriggerEvent]
    :param status: The current status of trigger. Possible values include:
     'Disabled', 'Enabled'. Default value: "Enabled" .
    :type status: str or
     ~azure.mgmt.containerregistry.v2019_04_01.models.TriggerStatus
    :param name: The name of the trigger.
    :type name: str
    """

    _validation = {
        'source_repository': {'required': True},
        'source_trigger_events': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'source_repository': {'key': 'sourceRepository', 'type': 'SourceProperties'},
        'source_trigger_events': {'key': 'sourceTriggerEvents', 'type': '[str]'},
        'status': {'key': 'status', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, source_repository, source_trigger_events, name, status="Enabled"):
        super(SourceTrigger, self).__init__()
        self.source_repository = source_repository
        self.source_trigger_events = source_trigger_events
        self.status = status
        self.name = name
