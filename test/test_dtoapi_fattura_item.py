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

from openapi_client.models.dtoapi_fattura_item import DTOAPIFatturaItem

class TestDTOAPIFatturaItem(unittest.TestCase):
    """DTOAPIFatturaItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DTOAPIFatturaItem:
        """Test DTOAPIFatturaItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DTOAPIFatturaItem`
        """
        model = DTOAPIFatturaItem()
        if include_optional:
            return DTOAPIFatturaItem(
                prodotto = openapi_client.models.dtoapi_prodotto.DTOAPIProdotto(
                    nome_prodotto = '', 
                    categoria = openapi_client.models.dtoapi_categoria.DTOAPICategoria(
                        id = 56, ), ),
                quantit_singolo = 1.337,
                unita_qnt_singolo = openapi_client.models.dtoapi_unita_misura.DTOAPIUnitaMisura(
                    id = 56, 
                    descrizione = '', 
                    sigla = '', ),
                tipologia_iva = openapi_client.models.dtoapi_categoria.DTOAPICategoria(
                    id = 56, 
                    categoria = '', ),
                esenzione_iva = openapi_client.models.dtoapi_categoria.DTOAPICategoria(
                    id = 56, 
                    categoria = '', ),
                prezzo_singolo = 1.337,
                prezzo_totale = 1.337,
                sconto = 1.337,
                tipo_sconto = 56,
                iva = 1.337,
                codice_commerciale = '',
                nome_commerciale = '',
                tipo_retta_entita = openapi_client.models.dtoapi_categoria.DTOAPICategoria(
                    id = 56, 
                    categoria = '', ),
                mese = 56,
                anno = 56
            )
        else:
            return DTOAPIFatturaItem(
        )
        """

    def testDTOAPIFatturaItem(self):
        """Test DTOAPIFatturaItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
