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

from openapi_client.models.dtoapi_visita_paziente import DTOAPIVisitaPaziente

class TestDTOAPIVisitaPaziente(unittest.TestCase):
    """DTOAPIVisitaPaziente unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DTOAPIVisitaPaziente:
        """Test DTOAPIVisitaPaziente
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DTOAPIVisitaPaziente`
        """
        model = DTOAPIVisitaPaziente()
        if include_optional:
            return DTOAPIVisitaPaziente(
                id = 56,
                codice_fiscale = '',
                nome = '',
                cognome = '',
                data_nascita = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                comune_nascita = '',
                stato_coscienza = True
            )
        else:
            return DTOAPIVisitaPaziente(
        )
        """

    def testDTOAPIVisitaPaziente(self):
        """Test DTOAPIVisitaPaziente"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
