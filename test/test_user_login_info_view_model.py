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

from openapi_client.models.user_login_info_view_model import UserLoginInfoViewModel

class TestUserLoginInfoViewModel(unittest.TestCase):
    """UserLoginInfoViewModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserLoginInfoViewModel:
        """Test UserLoginInfoViewModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserLoginInfoViewModel`
        """
        model = UserLoginInfoViewModel()
        if include_optional:
            return UserLoginInfoViewModel(
                login_provider = '',
                provider_key = ''
            )
        else:
            return UserLoginInfoViewModel(
        )
        """

    def testUserLoginInfoViewModel(self):
        """Test UserLoginInfoViewModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
