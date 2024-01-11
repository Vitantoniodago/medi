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

from openapi_client.models.dtoapi_bisogni_paziente import DTOAPIBisogniPaziente

class TestDTOAPIBisogniPaziente(unittest.TestCase):
    """DTOAPIBisogniPaziente unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DTOAPIBisogniPaziente:
        """Test DTOAPIBisogniPaziente
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DTOAPIBisogniPaziente`
        """
        model = DTOAPIBisogniPaziente()
        if include_optional:
            return DTOAPIBisogniPaziente(
                bisogni_paziente_aliemntazione = [
                    openapi_client.models.dto_bisogni_paziente_alimentazione.DTOBisogniPazienteAlimentazione(
                        assenza_alimentazione = True, 
                        alimentazione_orale = True, 
                        ausili_alimentazione = True, 
                        imboccato = True, 
                        dieta_specifica = True, 
                        dieta_sbilanciata = True, 
                        ematemesi = True, 
                        meteorismo = True, 
                        protesi_dentaria = True, 
                        nutrizione_parentale = True, 
                        nutrizione_enterale = True, 
                        melena = True, 
                        sondino = True, 
                        rifiuto_cibo = True, 
                        calo_ponderale = True, 
                        id_gastrectomia = 56, 
                        id_diabete = 56, 
                        intolleranze_alimentari = '', 
                        impedimento_alimentazione = '', 
                        note = '', 
                        id_analisi_bisogni_alimentazione = 56, 
                        id_assistito = 56, 
                        id_visita = 56, )
                    ],
                bisogni_paziente_comunicazione = [
                    openapi_client.models.dto_bisogni_paziente_comunicazione.DTOBisogniPazienteComunicazione(
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
                        id_visita = 56, )
                    ],
                bisogni_paziente_eliminazione = [
                    openapi_client.models.dto_bisogni_paziente_eliminazione.DTOBisogniPazienteEliminazione(
                        ano_preternaturale = True, 
                        proctorragia = True, 
                        caterismo_intermittente = True, 
                        ritenzione_urinaria = True, 
                        catetere_vescicale = True, 
                        stipsi = True, 
                        dolori_addominali = True, 
                        tenesmo_rettale = True, 
                        drenaggio_transcutaneo = True, 
                        tenesmo_vescicale = True, 
                        ematuria = True, 
                        ureterostomie = True, 
                        id_incontinenza_fecale = 56, 
                        id_incontenenza_urinaria = 56, 
                        note = '', 
                        id_analisi_bisogni_eliminazione = 56, 
                        id_assistito = 56, 
                        id_visita = 56, )
                    ],
                bisogni_paziente_igiene = [
                    openapi_client.models.dto_bisogni_paziente_igiene.DTOBisogniPazienteIgiene(
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
                        id_visita = 56, )
                    ],
                bisogni_paziente_mobilizzazione = [
                    openapi_client.models.dto_bisogni_paziente_mobilizzazione.DTOBisogniPazienteMobilizzazione(
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
                        id_visita = 56, )
                    ],
                bisogni_paziente_sicurezza_sonno = [
                    openapi_client.models.dto_bisogni_paziente_sicurezza_sonno.DTOBisogniPazienteSicurezzaSonno(
                        alterazione_sonno = True, 
                        allettato_con_sponde = True, 
                        rischio_infezione = True, 
                        insonnia = True, 
                        infezione_in_atto = True, 
                        agitazione = True, 
                        malattia_contagiosa = True, 
                        defedamento = True, 
                        sovrappeso = True, 
                        rischio_caduta = True, 
                        note = '', 
                        id_analisi_bisogni_sicurezza_sonno = 56, 
                        id_assistito = 56, 
                        id_visita = 56, )
                    ]
            )
        else:
            return DTOAPIBisogniPaziente(
        )
        """

    def testDTOAPIBisogniPaziente(self):
        """Test DTOAPIBisogniPaziente"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
