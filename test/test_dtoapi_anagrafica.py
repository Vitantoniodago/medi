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

from openapi_client.models.dtoapi_anagrafica import DTOAPIAnagrafica

class TestDTOAPIAnagrafica(unittest.TestCase):
    """DTOAPIAnagrafica unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DTOAPIAnagrafica:
        """Test DTOAPIAnagrafica
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DTOAPIAnagrafica`
        """
        model = DTOAPIAnagrafica()
        if include_optional:
            return DTOAPIAnagrafica(
                codice_fiscale = '',
                nome = '',
                cognome = '',
                comune = '',
                provincia = '',
                indirizzo = '',
                cap = ''
            )
        else:
            return DTOAPIAnagrafica(
        )
        """

    def testDTOAPIAnagrafica(self):
        """Test DTOAPIAnagrafica"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
