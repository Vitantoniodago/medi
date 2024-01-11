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

from openapi_client.models.dtoapi_fattura import DTOAPIFattura

class TestDTOAPIFattura(unittest.TestCase):
    """DTOAPIFattura unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DTOAPIFattura:
        """Test DTOAPIFattura
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DTOAPIFattura`
        """
        model = DTOAPIFattura()
        if include_optional:
            return DTOAPIFattura(
                data_fatturazione = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                data_creazione = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                categoria_documento = openapi_client.models.dtoapi_categoria.DTOAPICategoria(
                    id = 56, 
                    categoria = '', ),
                codice_documento = '',
                mittente = openapi_client.models.dtoapi_azienda.DTOAPIAzienda(
                    ragione_sociale = '', 
                    codice_azienda = '', 
                    partita_iva = '', 
                    codice_fiscale = '', 
                    indirizzo = '', 
                    pec = '', 
                    email = '', 
                    comune = '', 
                    provincia = '', 
                    cap = '', 
                    sede_riferimento = '', 
                    categoria = openapi_client.models.dtoapi_categoria.DTOAPICategoria(
                        id = 56, ), ),
                destinatario = openapi_client.models.dtoapi_azienda.DTOAPIAzienda(
                    ragione_sociale = '', 
                    codice_azienda = '', 
                    partita_iva = '', 
                    codice_fiscale = '', 
                    indirizzo = '', 
                    pec = '', 
                    email = '', 
                    comune = '', 
                    provincia = '', 
                    cap = '', 
                    sede_riferimento = '', 
                    categoria = openapi_client.models.dtoapi_categoria.DTOAPICategoria(
                        id = 56, ), ),
                item_fattura = [
                    openapi_client.models.dtoapi_fattura_item.DTOAPIFatturaItem(
                        prodotto = openapi_client.models.dtoapi_prodotto.DTOAPIProdotto(
                            nome_prodotto = '', 
                            categoria = openapi_client.models.dtoapi_categoria.DTOAPICategoria(
                                id = 56, ), ), 
                        quantitàsingolo = 1.337, 
                        unita_qnt_singolo = openapi_client.models.dtoapi_unita_misura.DTOAPIUnitaMisura(
                            id = 56, 
                            descrizione = '', 
                            sigla = '', ), 
                        tipologia_iva = openapi_client.models.dtoapi_categoria.DTOAPICategoria(
                            id = 56, ), 
                        esenzione_iva = , 
                        prezzo_singolo = 1.337, 
                        prezzo_totale = 1.337, 
                        sconto = 1.337, 
                        tipo_sconto = 56, 
                        iva = 1.337, 
                        codice_commerciale = '', 
                        nome_commerciale = '', 
                        tipo_retta_entita = , 
                        mese = 56, 
                        anno = 56, )
                    ],
                sub_totale = 1.337,
                totale_iva = 1.337,
                totale_sconto = 1.337,
                totale = 1.337,
                note = '',
                stato_pagamento = openapi_client.models.dtoapi_categoria.DTOAPICategoria(
                    id = 56, 
                    categoria = '', ),
                tipologia_pagamento = openapi_client.models.dtoapi_categoria.DTOAPICategoria(
                    id = 56, 
                    categoria = '', ),
                condizioni_pagamento = openapi_client.models.dtoapi_categoria.DTOAPICategoria(
                    id = 56, 
                    categoria = '', ),
                assistito = openapi_client.models.dtoapi_anagrafica.DTOAPIAnagrafica(
                    codice_fiscale = '', 
                    nome = '', 
                    cognome = '', 
                    comune = '', 
                    provincia = '', 
                    indirizzo = '', 
                    cap = '', )
            )
        else:
            return DTOAPIFattura(
        )
        """

    def testDTOAPIFattura(self):
        """Test DTOAPIFattura"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()