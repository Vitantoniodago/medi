# coding: utf-8

"""
    MediHome-CloudServer

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.add_external_login_binding_model import AddExternalLoginBindingModel

class TestAddExternalLoginBindingModel(unittest.TestCase):
    """AddExternalLoginBindingModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddExternalLoginBindingModel:
        """Test AddExternalLoginBindingModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddExternalLoginBindingModel`
        """
        model = AddExternalLoginBindingModel()
        if include_optional:
            return AddExternalLoginBindingModel(
                external_access_token = ''
            )
        else:
            return AddExternalLoginBindingModel(
                external_access_token = '',
        )
        """

    def testAddExternalLoginBindingModel(self):
        """Test AddExternalLoginBindingModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()