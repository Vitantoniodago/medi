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

from openapi_client.models.dto_patologica_remota_malattie import DTOPatologicaRemotaMalattie

class TestDTOPatologicaRemotaMalattie(unittest.TestCase):
    """DTOPatologicaRemotaMalattie unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DTOPatologicaRemotaMalattie:
        """Test DTOPatologicaRemotaMalattie
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DTOPatologicaRemotaMalattie`
        """
        model = DTOPatologicaRemotaMalattie()
        if include_optional:
            return DTOPatologicaRemotaMalattie(
                diagnosi = '',
                id_stato_malattia = 56,
                eta_malattia = 1.337,
                note = '',
                id_patologica_remota_malattie = 56,
                id_assistito = 56,
                id_visita = 56
            )
        else:
            return DTOPatologicaRemotaMalattie(
        )
        """

    def testDTOPatologicaRemotaMalattie(self):
        """Test DTOPatologicaRemotaMalattie"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
