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

from .event_info import EventInfo


class Event(EventInfo):
    """The event for a webhook.

    :param id: The event ID.
    :type id: str
    :param event_request_message: The event request message sent to the
     service URI.
    :type event_request_message:
     ~azure.mgmt.containerregistry.v2018_09_01.models.EventRequestMessage
    :param event_response_message: The event response message received from
     the service URI.
    :type event_response_message:
     ~azure.mgmt.containerregistry.v2018_09_01.models.EventResponseMessage
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'event_request_message': {'key': 'eventRequestMessage', 'type': 'EventRequestMessage'},
        'event_response_message': {'key': 'eventResponseMessage', 'type': 'EventResponseMessage'},
    }

    def __init__(self, id=None, event_request_message=None, event_response_message=None):
        super(Event, self).__init__(id=id)
        self.event_request_message = event_request_message
        self.event_response_message = event_response_message