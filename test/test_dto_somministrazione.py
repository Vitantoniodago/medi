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

from openapi_client.models.dto_somministrazione import DTOSomministrazione

class TestDTOSomministrazione(unittest.TestCase):
    """DTOSomministrazione unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DTOSomministrazione:
        """Test DTOSomministrazione
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DTOSomministrazione`
        """
        model = DTOSomministrazione()
        if include_optional:
            return DTOSomministrazione(
                id_somministrazione = 56,
                prescrizione = openapi_client.models.dto_prescrizione.DTOPrescrizione(
                    id_farmaco = 56, 
                    farmaco = '', 
                    id_unita = 56, 
                    id_modalita_somministrazione = 56, 
                    id_via_somministrazione = 56, 
                    inizio_terapia = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    fine_terapia = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    durata_terapia = 56, 
                    note = '', 
                    id_assistito = 56, 
                    id_prescrizione = 56, 
                    id_modalita_ora_somministrazione = 56, 
                    modelli = [
                        openapi_client.models.dto_item_prescrizione.DTOItemPrescrizione(
                            id_item_prescrizione = 56, 
                            id_prescrizione = 56, 
                            time_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            time_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            lunedi = True, 
                            martedi = True, 
                            mercoledi = True, 
                            giovedi = True, 
                            venerdi = True, 
                            sabato = True, 
                            domenica = True, )
                        ], 
                    somministrazione_colazione = True, 
                    somministrato = True, 
                    ora_colazione = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    somministrazione_pranzo = True, 
                    ora_pranzo = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    somministrazione_cena = True, 
                    ora_cena = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    ora_inizio = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    ora_fine = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id_visita = 56, 
                    assistito = openapi_client.models.dtoapi_assistito.DTOAPIAssistito(
                        guid_assistito = '', 
                        id_assistito = 56, 
                        nome = '', 
                        cognome = '', 
                        codice_fiscale = '', 
                        data_nascita = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        sesso = 56, 
                        comune = '', 
                        indirizzo = '', 
                        cap = '', 
                        anamnesi = openapi_client.models.dtoapi_anamnesi.DTOAPIAnamnesi(
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
                                ], ), 
                        esami_obiettivo = openapi_client.models.dtoapi_esami_obiettivo.DTOAPIEsamiObiettivo(
                            esame_obiettivo_generale = [
                                openapi_client.models.dto_esame_obiettivo_generale.DTOEsameObiettivoGenerale(
                                    data_visita = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    altezza = 1.337, 
                                    peso = 1.337, 
                                    bmi = 1.337, 
                                    stato_nutrizione = '', 
                                    circonferenza_addominale = 1.337, 
                                    temperatura = 1.337, 
                                    id_localizzazione_temperatura = 56, 
                                    pa_sistolica = 1.337, 
                                    pa_diastolica = 1.337, 
                                    freq_respiro = 1.337, 
                                    freq_cardiaca = 1.337, 
                                    id_stato_generale = '', 
                                    note = '', 
                                    id_assistito = 56, 
                                    id_esame_obiettivo_generale = 56, 
                                    id_decubito = '', 
                                    id_mucose = '', 
                                    id_masse_muscolari = '', 
                                    id_polso = '', 
                                    id_stato_psichico = '', 
                                    id_cute = '', 
                                    id_sottocute = '', 
                                    id_lingua = '', 
                                    id_respiro = '', 
                                    id_visita = 56, )
                                ], 
                            esame_obiettivo_regionale = [
                                openapi_client.models.dto_esame_obiettivo_regionale.DTOEsameObiettivoRegionale(
                                    id_assistito = 56, 
                                    id_esame_obiettivo_regionale = 56, 
                                    idmv_polmone_destro = '', 
                                    idfvt_polmone_destro = '', 
                                    id_percussione_polmone_destro = '', 
                                    id_rumori_patologici_polmone_destro = '', 
                                    id_sede_polmone_destro = '', 
                                    idmv_polmone_sinistro = '', 
                                    idfvt_polmone_sinistro = '', 
                                    id_percussione_polmone_sinistro = '', 
                                    id_rumori_patologici_polmone_sinistro = '', 
                                    id_sede_polmone_sinistro = '', 
                                    id_tono = '', 
                                    id_soffi = '', 
                                    id_apparato_urogenitale = '', 
                                    id_addome = '', 
                                    id_occhi = 56, 
                                    id_vista = 56, 
                                    note_vista = '', 
                                    id_cavo_orale = 56, 
                                    orecchio = '', 
                                    id_udito = 56, 
                                    note_udito = '', 
                                    id_collo = 56, 
                                    sistema_arterioso = '', 
                                    sistema_venoso_linfatico = '', 
                                    apparato_muscolo_scheletrico = '', 
                                    alterazione_podologica = '', 
                                    id_tono_sistema_nervoso = 56, 
                                    note_tono_sistema_nervoso = '', 
                                    id_movimenti = 56, 
                                    id_visita = 56, )
                                ], ), 
                        esami_strumentali = openapi_client.models.dtoapi_esami_strumentale.DTOAPIEsamiStrumentale(
                            esame_strumentale_conclusione = [
                                openapi_client.models.dto_esame_strumentale_conclusione_terapia.DTOEsameStrumentaleConclusioneTerapia(
                                    id_conclusione_terapia = 56, 
                                    id_assistito = 56, 
                                    note_conclusioni = '', 
                                    conclusioni = '', 
                                    consigli_terapia = '', 
                                    id_referto = 56, 
                                    id_visita = 56, )
                                ], ), 
                        prescrizioni = openapi_client.models.dtoapi_prescrizioni.DTOAPIPrescrizioni(), 
                        somministrazioni = openapi_client.models.dtoapi_somministrazioni.DTOAPISomministrazioni(
                            somministrazione = [
                                openapi_client.models.dto_somministrazione.DTOSomministrazione(
                                    id_somministrazione = 56, 
                                    modelli_parziali = [
                                        openapi_client.models.dto_modello_parziale.DTOModelloParziale(
                                            time_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            time_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            settimana = [
                                                True
                                                ], 
                                            gg_settimana = 56, )
                                        ], )
                                ], ), 
                        prestazioni_fisioterapiche = openapi_client.models.dtoapi_prestazioni_fisioterapiche.DTOAPIPrestazioniFisioterapiche(
                            prestazione_fisioterapica = [
                                openapi_client.models.dto_prestazione.DTOPrestazione(
                                    id_prestazione = 56, 
                                    id_prestazione_planning = 56, 
                                    id_equipe = 56, 
                                    id_pai = 56, 
                                    id_frequenza = 56, 
                                    durata = 1.337, 
                                    codice = '', 
                                    descrizione = '', 
                                    inizio_prestazione = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    fine_prestazione = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    note_prestazione = '', 
                                    id_assistito = 56, 
                                    durata_prestazione = 56, 
                                    id_modalita_ora_prestazione = 56, 
                                    effettuata = True, 
                                    note_tipologia_accessi = '', 
                                    struttura_erogante = '', )
                                ], ), 
                        diari_clinici = openapi_client.models.dtoapi_diario_clinico.DTOAPIDiarioClinico(
                            diario_clinico = [
                                openapi_client.models.dto_diario_clinico.DTODiarioClinico(
                                    valido_da = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    valido_a = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    note = '', 
                                    id_diario_clinico = 56, 
                                    id_assistito = 56, 
                                    id_visita = 56, 
                                    priorita = 56, )
                                ], ), 
                        bisogni_paziente = openapi_client.models.dtoapi_bisogni_paziente.DTOAPIBisogniPaziente(
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
                                ], ), 
                        elenco_note = openapi_client.models.dtoapi_note.DTOAPINote(
                            note = [
                                ''
                                ], ), 
                        consensi = openapi_client.models.dtoapi_consensi.DTOAPIConsensi(
                            consenso = [
                                ''
                                ], ), 
                        sessione = openapi_client.models.dtoapi_session.DTOAPISession(
                            guid_session = '00000000-0000-0000-0000-000000000000', 
                            utente = openapi_client.models.dtoapi_user.DTOAPIUser(
                                guid = '', 
                                user_name = '', 
                                email = '', 
                                password = '', 
                                tipologia = '', 
                                api_key = '00000000-0000-0000-0000-000000000000', 
                                nome = '', 
                                cognome = '', 
                                ruolo = '', 
                                id_tipologia = 56, 
                                codice_fiscale = '', 
                                guid_medibox = '', ), 
                            start_session = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            expired = 56, ), ), ),
                modelli_parziali = [
                    openapi_client.models.dto_modello_parziale.DTOModelloParziale(
                        time_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        settimana = [
                            True
                            ], 
                        gg_settimana = 56, )
                    ]
            )
        else:
            return DTOSomministrazione(
        )
        """

    def testDTOSomministrazione(self):
        """Test DTOSomministrazione"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
