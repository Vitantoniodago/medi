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

from openapi_client.models.user_info_view_model import UserInfoViewModel

class TestUserInfoViewModel(unittest.TestCase):
    """UserInfoViewModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserInfoViewModel:
        """Test UserInfoViewModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserInfoViewModel`
        """
        model = UserInfoViewModel()
        if include_optional:
            return UserInfoViewModel(
                email = '',
                has_registered = True,
                login_provider = ''
            )
        else:
            return UserInfoViewModel(
        )
        """

    def testUserInfoViewModel(self):
        """Test UserInfoViewModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()