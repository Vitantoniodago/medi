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

from openapi_client.models.dto_bisogni_paziente_mobilizzazione import DTOBisogniPazienteMobilizzazione

class TestDTOBisogniPazienteMobilizzazione(unittest.TestCase):
    """DTOBisogniPazienteMobilizzazione unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DTOBisogniPazienteMobilizzazione:
        """Test DTOBisogniPazienteMobilizzazione
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DTOBisogniPazienteMobilizzazione`
        """
        model = DTOBisogniPazienteMobilizzazione()
        if include_optional:
            return DTOBisogniPazienteMobilizzazione(
                ausilio_letto = True,
                aiuto_seduta = True,
                movimenti_volontari = True,
                rotazione_corpo = True,
                aiuto_deambulazione = True,
                permanenza_letto_forzata = True,
                disabile_allettato = True,
                mobilizzazione_strumenti = True,
                lesioni_ossee = True,
                lombagia_acuta = True,
                cervicoalgia_acuta = True,
                paraplegia = True,
                emiplegia = True,
                tetraplegia = True,
                id_amputazione = 56,
                note_amputazione = '',
                note = '',
                id_analisi_bisogni_mobilizzazione = 56,
                id_assistito = 56,
                id_visita = 56
            )
        else:
            return DTOBisogniPazienteMobilizzazione(
        )
        """

    def testDTOBisogniPazienteMobilizzazione(self):
        """Test DTOBisogniPazienteMobilizzazione"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
