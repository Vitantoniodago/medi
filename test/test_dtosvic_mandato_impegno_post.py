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

from openapi_client.models.dtosvic_mandato_impegno_post import DTOSVICMandatoImpegnoPOST

class TestDTOSVICMandatoImpegnoPOST(unittest.TestCase):
    """DTOSVICMandatoImpegnoPOST unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DTOSVICMandatoImpegnoPOST:
        """Test DTOSVICMandatoImpegnoPOST
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DTOSVICMandatoImpegnoPOST`
        """
        model = DTOSVICMandatoImpegnoPOST()
        if include_optional:
            return DTOSVICMandatoImpegnoPOST(
                numero_impegno = '',
                anno_pagamento = 56,
                anno_competenza = 56,
                anno_assunzione = 56,
                dettaglio = [
                    openapi_client.models.dtosvic_riga_mandato.DTOSVICRigaMandato(
                        codice_creditore = '', 
                        importo = '', 
                        nota = '', )
                    ]
            )
        else:
            return DTOSVICMandatoImpegnoPOST(
        )
        """

    def testDTOSVICMandatoImpegnoPOST(self):
        """Test DTOSVICMandatoImpegnoPOST"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()