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

from .run_request import RunRequest


class TaskRunRequest(RunRequest):
    """The parameters for a task run request.

    :param is_archive_enabled: The value that indicates whether archiving is
     enabled for the run or not. Default value: False .
    :type is_archive_enabled: bool
    :param type: Constant filled by server.
    :type type: str
    :param task_name: The name of task against which run has to be queued.
    :type task_name: str
    :param values: The collection of overridable values that can be passed
     when running a task.
    :type values:
     list[~azure.mgmt.containerregistry.v2019_04_01.models.SetValue]
    """

    _validation = {
        'type': {'required': True},
        'task_name': {'required': True},
    }

    _attribute_map = {
        'is_archive_enabled': {'key': 'isArchiveEnabled', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'str'},
        'task_name': {'key': 'taskName', 'type': 'str'},
        'values': {'key': 'values', 'type': '[SetValue]'},
    }

    def __init__(self, task_name, is_archive_enabled=False, values=None):
        super(TaskRunRequest, self).__init__(is_archive_enabled=is_archive_enabled)
        self.task_name = task_name
        self.values = values
        self.type = 'TaskRunRequest'