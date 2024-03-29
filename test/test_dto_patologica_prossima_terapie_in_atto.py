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

from openapi_client.models.dto_patologica_prossima_terapie_in_atto import DTOPatologicaProssimaTerapieInAtto

class TestDTOPatologicaProssimaTerapieInAtto(unittest.TestCase):
    """DTOPatologicaProssimaTerapieInAtto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DTOPatologicaProssimaTerapieInAtto:
        """Test DTOPatologicaProssimaTerapieInAtto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DTOPatologicaProssimaTerapieInAtto`
        """
        model = DTOPatologicaProssimaTerapieInAtto()
        if include_optional:
            return DTOPatologicaProssimaTerapieInAtto(
                nessun_farmaco = True,
                id_farmaco = 56,
                quantita = '',
                frequenza_assunzione = 56,
                note = '',
                id_patologica_prossima_terapie_in_atto = 56,
                id_assistito = 56,
                id_visita = 56
            )
        else:
            return DTOPatologicaProssimaTerapieInAtto(
        )
        """

    def testDTOPatologicaProssimaTerapieInAtto(self):
        """Test DTOPatologicaProssimaTerapieInAtto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
