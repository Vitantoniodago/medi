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

from openapi_client.models.dto_bisogni_paziente_igiene import DTOBisogniPazienteIgiene

class TestDTOBisogniPazienteIgiene(unittest.TestCase):
    """DTOBisogniPazienteIgiene unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DTOBisogniPazienteIgiene:
        """Test DTOBisogniPazienteIgiene
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DTOBisogniPazienteIgiene`
        """
        model = DTOBisogniPazienteIgiene()
        if include_optional:
            return DTOBisogniPazienteIgiene(
                aiuto_igiene = True,
                strumenti_igiene = True,
                aiuto_bagno = True,
                bagno_letto = True,
                aiuto_vestizione = True,
                piaghe_decubito = True,
                aiuto_doccia = True,
                aiuto_shampoo = True,
                aiuto_pediluvio = True,
                aiuto_estetico = True,
                igiene_catetere = True,
                igiene_stormie = True,
                igiene_incontinenza = True,
                ustioni = '',
                ferite = '',
                malattie_pelle = '',
                note = '',
                id_analisi_bisogni_igiene = 56,
                id_assistito = 56,
                id_visita = 56
            )
        else:
            return DTOBisogniPazienteIgiene(
        )
        """

    def testDTOBisogniPazienteIgiene(self):
        """Test DTOBisogniPazienteIgiene"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
