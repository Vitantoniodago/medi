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

from openapi_client.models.manage_info_view_model import ManageInfoViewModel

class TestManageInfoViewModel(unittest.TestCase):
    """ManageInfoViewModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ManageInfoViewModel:
        """Test ManageInfoViewModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ManageInfoViewModel`
        """
        model = ManageInfoViewModel()
        if include_optional:
            return ManageInfoViewModel(
                local_login_provider = '',
                email = '',
                logins = [
                    openapi_client.models.user_login_info_view_model.UserLoginInfoViewModel(
                        login_provider = '', 
                        provider_key = '', )
                    ],
                external_login_providers = [
                    openapi_client.models.external_login_view_model.ExternalLoginViewModel(
                        name = '', 
                        url = '', 
                        state = '', )
                    ]
            )
        else:
            return ManageInfoViewModel(
        )
        """

    def testManageInfoViewModel(self):
        """Test ManageInfoViewModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()