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

from openapi_client.models.dtoapi_anamnesi import DTOAPIAnamnesi

class TestDTOAPIAnamnesi(unittest.TestCase):
    """DTOAPIAnamnesi unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DTOAPIAnamnesi:
        """Test DTOAPIAnamnesi
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DTOAPIAnamnesi`
        """
        model = DTOAPIAnamnesi()
        if include_optional:
            return DTOAPIAnamnesi(
                anamnesi_familiare = [
                    openapi_client.models.dto_anamnesi_familiare.DTOAnamnesiFamiliare(
                        id_anamnesi_familiare = 56, 
                        nega_presenza_patologia = True, 
                        id_parentela = 56, 
                        id_diagnosi = 56, 
                        deceduto = True, 
                        note = '', 
                        id_assistito = 56, 
                        eta = 56, 
                        id_ereditarieta = 56, 
                        id_visita = 56, )
                    ],
                patologica_prossima_terapia = [
                    openapi_client.models.dto_patologica_prossima_terapie_in_atto.DTOPatologicaProssimaTerapieInAtto(
                        nessun_farmaco = True, 
                        id_farmaco = 56, 
                        quantita = '', 
                        frequenza_assunzione = 56, 
                        note = '', 
                        id_patologica_prossima_terapie_in_atto = 56, 
                        id_assistito = 56, 
                        id_visita = 56, )
                    ],
                patologica_prossima_ulcere = [
                    openapi_client.models.dto_patologica_prossima_ulcere_da_pressione.DTOPatologicaProssimaUlcereDaPressione(
                        id_assistito = 56, 
                        sede = '', 
                        id_grado = 56, 
                        medicazione = '', 
                        id_patologica_prossima_ulcere_da_pressione = 56, 
                        id_visita = 56, )
                    ],
                patologica_remota_interventi_pregressi = [
                    openapi_client.models.dto_patologica_remota_interventi_pregressi.DTOPatologicaRemotaInterventiPregressi(
                        nega_intervento = True, 
                        intervento = '', 
                        data_intervento = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        eta = 1.337, 
                        patologia = '', 
                        note = '', 
                        id_patologica_remota_interventi_pregressi = 56, 
                        id_assistito = 56, 
                        id_visita = 56, )
                    ],
                patologica_remota_malattie = [
                    openapi_client.models.dto_patologica_remota_malattie.DTOPatologicaRemotaMalattie(
                        diagnosi = '', 
                        id_stato_malattia = 56, 
                        eta_malattia = 1.337, 
                        note = '', 
                        id_patologica_remota_malattie = 56, 
                        id_assistito = 56, 
                        id_visita = 56, )
                    ],
                patologica_remota_ricoveri_pregressi = [
                    openapi_client.models.dto_patologica_remota_ricoveri_pregressi.DTOPatologicaRemotaRicoveriPregressi(
                        data_ricovero = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        unita_ospedaliera = '', 
                        ospedale = '', 
                        id_patologica_remota_ricoveri_pregressi = 56, 
                        id_assistito = 56, 
                        id_visita = 56, )
                    ]
            )
        else:
            return DTOAPIAnamnesi(
        )
        """

    def testDTOAPIAnamnesi(self):
        """Test DTOAPIAnamnesi"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
