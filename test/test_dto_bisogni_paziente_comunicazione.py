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

from openapi_client.models.dto_bisogni_paziente_comunicazione import DTOBisogniPazienteComunicazione

class TestDTOBisogniPazienteComunicazione(unittest.TestCase):
    """DTOBisogniPazienteComunicazione unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DTOBisogniPazienteComunicazione:
        """Test DTOBisogniPazienteComunicazione
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DTOBisogniPazienteComunicazione`
        """
        model = DTOBisogniPazienteComunicazione()
        if include_optional:
            return DTOBisogniPazienteComunicazione(
                assenza_comunicazione = True,
                disturbi_uditivi = True,
                difficolta_comunicazione = True,
                sordomutismo = True,
                sensorio_obnubilato = True,
                trachestomia = True,
                cecita_bilaterale = True,
                stato_soporoso = True,
                portatore_lenti = True,
                stato_coma = True,
                glaucoma = True,
                mancanza_conoscenza_malattia = True,
                congiuntivite = True,
                preoccupazione_stato = True,
                otalgie = True,
                rapporto_difficile_parenti = True,
                sordita_bilaterale = True,
                preoccupazione_lavoro = True,
                protesi_fonetica = True,
                tossicodipendenza = True,
                protesi_acustica = True,
                alcoldipendenza = True,
                disturbi_linguaggio = True,
                stati_psicologici = '',
                alterazione_umore = '',
                note = '',
                id_analisi_bisogni_comunicazione = 56,
                id_assistito = 56,
                id_visita = 56
            )
        else:
            return DTOBisogniPazienteComunicazione(
        )
        """

    def testDTOBisogniPazienteComunicazione(self):
        """Test DTOBisogniPazienteComunicazione"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
