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

from openapi_client.models.dto_anamnesi_familiare import DTOAnamnesiFamiliare

class TestDTOAnamnesiFamiliare(unittest.TestCase):
    """DTOAnamnesiFamiliare unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DTOAnamnesiFamiliare:
        """Test DTOAnamnesiFamiliare
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DTOAnamnesiFamiliare`
        """
        model = DTOAnamnesiFamiliare()
        if include_optional:
            return DTOAnamnesiFamiliare(
                id_anamnesi_familiare = 56,
                nega_presenza_patologia = True,
                id_parentela = 56,
                id_diagnosi = 56,
                deceduto = True,
                note = '',
                id_assistito = 56,
                eta = 56,
                id_ereditarieta = 56,
                id_visita = 56
            )
        else:
            return DTOAnamnesiFamiliare(
        )
        """

    def testDTOAnamnesiFamiliare(self):
        """Test DTOAnamnesiFamiliare"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
