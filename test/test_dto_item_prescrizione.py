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

from openapi_client.models.dto_item_prescrizione import DTOItemPrescrizione

class TestDTOItemPrescrizione(unittest.TestCase):
    """DTOItemPrescrizione unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DTOItemPrescrizione:
        """Test DTOItemPrescrizione
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DTOItemPrescrizione`
        """
        model = DTOItemPrescrizione()
        if include_optional:
            return DTOItemPrescrizione(
                id_item_prescrizione = 56,
                id_prescrizione = 56,
                time_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                time_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                lunedi = True,
                martedi = True,
                mercoledi = True,
                giovedi = True,
                venerdi = True,
                sabato = True,
                domenica = True
            )
        else:
            return DTOItemPrescrizione(
        )
        """

    def testDTOItemPrescrizione(self):
        """Test DTOItemPrescrizione"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()