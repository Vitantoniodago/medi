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

from openapi_client.models.change_password_binding_model import ChangePasswordBindingModel

class TestChangePasswordBindingModel(unittest.TestCase):
    """ChangePasswordBindingModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChangePasswordBindingModel:
        """Test ChangePasswordBindingModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChangePasswordBindingModel`
        """
        model = ChangePasswordBindingModel()
        if include_optional:
            return ChangePasswordBindingModel(
                old_password = '',
                new_password = '012345',
                confirm_password = ''
            )
        else:
            return ChangePasswordBindingModel(
                old_password = '',
                new_password = '012345',
        )
        """

    def testChangePasswordBindingModel(self):
        """Test ChangePasswordBindingModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
