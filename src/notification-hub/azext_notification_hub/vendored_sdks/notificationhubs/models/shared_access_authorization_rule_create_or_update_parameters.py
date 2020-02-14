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


class SharedAccessAuthorizationRuleCreateOrUpdateParameters(Model):
    """Parameters supplied to the CreateOrUpdate Namespace AuthorizationRules.

    All required parameters must be populated in order to send to Azure.

    :param properties: Required. Properties of the Namespace
     AuthorizationRules.
    :type properties:
     ~azure.mgmt.notificationhubs.models.SharedAccessAuthorizationRuleProperties
    """

    _validation = {
        'properties': {'required': True},
    }

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'SharedAccessAuthorizationRuleProperties'},
    }

    def __init__(self, **kwargs):
        super(SharedAccessAuthorizationRuleCreateOrUpdateParameters, self).__init__(**kwargs)
        self.properties = kwargs.get('properties', None)
