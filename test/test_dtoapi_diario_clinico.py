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

from openapi_client.models.dtoapi_diario_clinico import DTOAPIDiarioClinico

class TestDTOAPIDiarioClinico(unittest.TestCase):
    """DTOAPIDiarioClinico unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DTOAPIDiarioClinico:
        """Test DTOAPIDiarioClinico
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DTOAPIDiarioClinico`
        """
        model = DTOAPIDiarioClinico()
        if include_optional:
            return DTOAPIDiarioClinico(
                diario_clinico = [
                    openapi_client.models.dto_diario_clinico.DTODiarioClinico(
                        valido_da = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        valido_a = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        note = '', 
                        id_diario_clinico = 56, 
                        id_assistito = 56, 
                        id_visita = 56, 
                        priorita = 56, )
                    ]
            )
        else:
            return DTOAPIDiarioClinico(
        )
        """

    def testDTOAPIDiarioClinico(self):
        """Test DTOAPIDiarioClinico"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
