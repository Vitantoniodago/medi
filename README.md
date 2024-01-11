# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://cloud.medihome.it
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.medihome.it"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountApi(api_client)
    model = openapi_client.AddExternalLoginBindingModel() # AddExternalLoginBindingModel | Modello di dati per login esterna

    try:
        # Aggiunta di una servizio di login esterno
        api_response = api_instance.account_add_external_login(model)
        print("The response of AccountApi->account_add_external_login:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->account_add_external_login: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://cloud.medihome.it*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**account_add_external_login**](docs/AccountApi.md#account_add_external_login) | **POST** /api/Account/AddExternalLogin | Aggiunta di una servizio di login esterno
*AccountApi* | [**account_change_password**](docs/AccountApi.md#account_change_password) | **POST** /api/Account/ChangePassword | Cambia la password utente
*AccountApi* | [**account_get_external_login**](docs/AccountApi.md#account_get_external_login) | **GET** /api/Account/ExternalLogin | Accesso tramite provider di terze parti
*AccountApi* | [**account_get_external_logins**](docs/AccountApi.md#account_get_external_logins) | **GET** /api/Account/ExternalLogins | Accesso tramite provider di terze parti
*AccountApi* | [**account_get_manage_info**](docs/AccountApi.md#account_get_manage_info) | **GET** /api/Account/ManageInfo | Restituisce le informazioni di managment dell&#39;utente
*AccountApi* | [**account_get_user_info**](docs/AccountApi.md#account_get_user_info) | **GET** /api/Account/UserInfo | Restituisce le informazioni dell&#39;utente
*AccountApi* | [**account_login**](docs/AccountApi.md#account_login) | **POST** /api/Account/Session | Login di uno specifico utente
*AccountApi* | [**account_logout**](docs/AccountApi.md#account_logout) | **POST** /api/Account/Logout | Disconnetti istanza
*AccountApi* | [**account_register**](docs/AccountApi.md#account_register) | **POST** /api/Account/Register | Registra un nuovo utente per l&#39;accesso al sistema
*AccountApi* | [**account_register_external**](docs/AccountApi.md#account_register_external) | **POST** /api/Account/RegisterExternal | Registers the external.
*AccountApi* | [**account_remove_login**](docs/AccountApi.md#account_remove_login) | **POST** /api/Account/RemoveLogin | Rimuovere una login esterna
*AccountApi* | [**account_set_password**](docs/AccountApi.md#account_set_password) | **POST** /api/Account/SetPassword | Imposta la password
*ArchivioParametriApi* | [**archivio_parametri_check_prestazione**](docs/ArchivioParametriApi.md#archivio_parametri_check_prestazione) | **POST** /api/ArchivioParametri/CheckPrestazione | Controllo della prestazione
*ArchivioParametriApi* | [**archivio_parametri_crea_prestazione**](docs/ArchivioParametriApi.md#archivio_parametri_crea_prestazione) | **POST** /api/ArchivioParametri/CreaPrestazione | Crea una prestazione.
*ArchivioParametriApi* | [**archivio_parametri_interrompi_prestazione**](docs/ArchivioParametriApi.md#archivio_parametri_interrompi_prestazione) | **POST** /api/ArchivioParametri/InterrompiPrestazione | Interrompi la prestazione.
*ArchivioParametriApi* | [**archivio_parametri_invio_parametro**](docs/ArchivioParametriApi.md#archivio_parametri_invio_parametro) | **POST** /api/ArchivioParametri/InvioParametro | Salvataggio di un parametro rilevato
*ArchivioParametriApi* | [**archivio_parametri_invio_set_parametri**](docs/ArchivioParametriApi.md#archivio_parametri_invio_set_parametri) | **POST** /api/ArchivioParametri/InvioSetParametri | Salvataggio di un set di parametri rilevato
*ArchivioParametriApi* | [**archivio_parametri_parametri_rilevati**](docs/ArchivioParametriApi.md#archivio_parametri_parametri_rilevati) | **POST** /api/ArchivioParametri/ParametriRilevati | Elenco dei parametri di un intervento.
*AssistitoApi* | [**assistito_lista**](docs/AssistitoApi.md#assistito_lista) | **POST** /api/Assistito/Lista | 
*AssistitoApi* | [**assistito_scheda**](docs/AssistitoApi.md#assistito_scheda) | **POST** /api/Assistito/Scheda | 
*AssistitoApi* | [**assistito_somministrazioni**](docs/AssistitoApi.md#assistito_somministrazioni) | **POST** /api/Assistito/Somministrazioni | 
*AttivitaDomiciliareApi* | [**attivita_domiciliare_interventi**](docs/AttivitaDomiciliareApi.md#attivita_domiciliare_interventi) | **POST** /api/AttivitaDomiciliare/Interventi | Lista degli interventi con richiesta parametrizzata
*AttivitaDomiciliareApi* | [**attivita_domiciliare_interventi1**](docs/AttivitaDomiciliareApi.md#attivita_domiciliare_interventi1) | **GET** /api/AttivitaDomiciliare/Interventi/{id} | Lista degli interventi di un assistito
*AttivitaDomiciliareApi* | [**attivita_domiciliare_interventi_assistito**](docs/AttivitaDomiciliareApi.md#attivita_domiciliare_interventi_assistito) | **POST** /api/AttivitaDomiciliare/InterventiAssistito | Lista degli interventi di un assistito con richiesta parametrizzata
*AttivitaDomiciliareApi* | [**attivita_domiciliare_prossimo_intervento**](docs/AttivitaDomiciliareApi.md#attivita_domiciliare_prossimo_intervento) | **POST** /api/AttivitaDomiciliare/ProssimoIntervento | Prossimo intervento.
*AttivitaDomiciliareApi* | [**attivita_domiciliare_prossimo_intervento_assistito**](docs/AttivitaDomiciliareApi.md#attivita_domiciliare_prossimo_intervento_assistito) | **POST** /api/AttivitaDomiciliare/ProssimoInterventoAssistito | Prossimo intervento di un assistito.
*DeviceApi* | [**device_licenza**](docs/DeviceApi.md#device_licenza) | **POST** /api/Device/Licenza | 
*DocumentiApi* | [**documenti_fattura**](docs/DocumentiApi.md#documenti_fattura) | **POST** /api/Documenti/Fattura | 
*DocumentiApi* | [**documenti_fatture**](docs/DocumentiApi.md#documenti_fatture) | **POST** /api/Documenti/Fatture | 
*EmergenzaApi* | [**emergenza_crea_visita**](docs/EmergenzaApi.md#emergenza_crea_visita) | **POST** /api/Emergenza/CreaVisita | 
*PrestazioneDomiciliareApi* | [**prestazione_domiciliare_avvio_prestazione**](docs/PrestazioneDomiciliareApi.md#prestazione_domiciliare_avvio_prestazione) | **POST** /api/PrestazioneDomiciliare/AvvioPrestazione | Avvio di una prestazione domiciliare.
*PrestazioneDomiciliareApi* | [**prestazione_domiciliare_check_prestazione**](docs/PrestazioneDomiciliareApi.md#prestazione_domiciliare_check_prestazione) | **POST** /api/PrestazioneDomiciliare/CheckPrestazione | Controllo della prestazione
*PrestazioneDomiciliareApi* | [**prestazione_domiciliare_interrompi_prestazione**](docs/PrestazioneDomiciliareApi.md#prestazione_domiciliare_interrompi_prestazione) | **POST** /api/PrestazioneDomiciliare/InterrompiPrestazione | Interrompi la prestazione domiciliare.
*PrestazioneDomiciliareApi* | [**prestazione_domiciliare_invio_parametro**](docs/PrestazioneDomiciliareApi.md#prestazione_domiciliare_invio_parametro) | **POST** /api/PrestazioneDomiciliare/InvioParametro | Salvataggio di un parametro rilevato
*PrestazioneDomiciliareApi* | [**prestazione_domiciliare_invio_set_parametri**](docs/PrestazioneDomiciliareApi.md#prestazione_domiciliare_invio_set_parametri) | **POST** /api/PrestazioneDomiciliare/InvioSetParametri | Salvataggio di un set di parametri rilevato
*PrestazioneDomiciliareApi* | [**prestazione_domiciliare_parametri_rilevati**](docs/PrestazioneDomiciliareApi.md#prestazione_domiciliare_parametri_rilevati) | **POST** /api/PrestazioneDomiciliare/ParametriRilevati | Elenco dei parametri di un intervento.
*SVICApi* | [**s_vic_budget**](docs/SVICApi.md#s_vic_budget) | **POST** /api/SVIC/Budget | 
*SVICApi* | [**s_vic_debitore**](docs/SVICApi.md#s_vic_debitore) | **POST** /api/finanziaria/debitore | 
*SVICApi* | [**s_vic_get_anagrafica**](docs/SVICApi.md#s_vic_get_anagrafica) | **GET** /api/finanziaria/anagrafica | 
*SVICApi* | [**s_vic_mandato**](docs/SVICApi.md#s_vic_mandato) | **GET** /api/finanziaria/mandato | 
*SVICApi* | [**s_vic_mandato_da_impegno**](docs/SVICApi.md#s_vic_mandato_da_impegno) | **POST** /api/finanziaria/mandatodaimpegno | 
*SVICApi* | [**s_vic_mandato_spesa_fissa**](docs/SVICApi.md#s_vic_mandato_spesa_fissa) | **POST** /api/finanziaria/mandatospesafissa | 
*SVICApi* | [**s_vic_movimentazione**](docs/SVICApi.md#s_vic_movimentazione) | **POST** /api/SVIC/Movimentazione | 
*SVICApi* | [**s_vic_reversale**](docs/SVICApi.md#s_vic_reversale) | **POST** /api/finanziaria/reversale | 
*SVICApi* | [**s_vic_reversale1**](docs/SVICApi.md#s_vic_reversale1) | **GET** /api/finanziaria/reversale | 
*SVICApi* | [**s_vic_set_anagrafica**](docs/SVICApi.md#s_vic_set_anagrafica) | **POST** /api/finanziaria/anagrafica | 
*SomministrazioneApi* | [**somministrazione_planning**](docs/SomministrazioneApi.md#somministrazione_planning) | **POST** /api/Somministrazione/Planning | 


## Documentation For Models

 - [AddExternalLoginBindingModel](docs/AddExternalLoginBindingModel.md)
 - [ChangePasswordBindingModel](docs/ChangePasswordBindingModel.md)
 - [DTOAPIAnagrafica](docs/DTOAPIAnagrafica.md)
 - [DTOAPIAnamnesi](docs/DTOAPIAnamnesi.md)
 - [DTOAPIAssistito](docs/DTOAPIAssistito.md)
 - [DTOAPIAttivitaEsterna](docs/DTOAPIAttivitaEsterna.md)
 - [DTOAPIAzienda](docs/DTOAPIAzienda.md)
 - [DTOAPIBisogniPaziente](docs/DTOAPIBisogniPaziente.md)
 - [DTOAPICategoria](docs/DTOAPICategoria.md)
 - [DTOAPIConsensi](docs/DTOAPIConsensi.md)
 - [DTOAPIDevice](docs/DTOAPIDevice.md)
 - [DTOAPIDiarioClinico](docs/DTOAPIDiarioClinico.md)
 - [DTOAPIDocumento](docs/DTOAPIDocumento.md)
 - [DTOAPIEsamiObiettivo](docs/DTOAPIEsamiObiettivo.md)
 - [DTOAPIEsamiStrumentale](docs/DTOAPIEsamiStrumentale.md)
 - [DTOAPIFattura](docs/DTOAPIFattura.md)
 - [DTOAPIFatturaItem](docs/DTOAPIFatturaItem.md)
 - [DTOAPIFiltriDocumento](docs/DTOAPIFiltriDocumento.md)
 - [DTOAPIInterventoDomiciliare](docs/DTOAPIInterventoDomiciliare.md)
 - [DTOAPILicenza](docs/DTOAPILicenza.md)
 - [DTOAPINote](docs/DTOAPINote.md)
 - [DTOAPIOperatore](docs/DTOAPIOperatore.md)
 - [DTOAPIParametroPrestazione](docs/DTOAPIParametroPrestazione.md)
 - [DTOAPIPrescrizioni](docs/DTOAPIPrescrizioni.md)
 - [DTOAPIPrestazione](docs/DTOAPIPrestazione.md)
 - [DTOAPIPrestazioniFisioterapiche](docs/DTOAPIPrestazioniFisioterapiche.md)
 - [DTOAPIProdotto](docs/DTOAPIProdotto.md)
 - [DTOAPIRichiestaInterventi](docs/DTOAPIRichiestaInterventi.md)
 - [DTOAPIRichiestaParametri](docs/DTOAPIRichiestaParametri.md)
 - [DTOAPIRichiestaSomministrazioni](docs/DTOAPIRichiestaSomministrazioni.md)
 - [DTOAPISession](docs/DTOAPISession.md)
 - [DTOAPISomministrazioni](docs/DTOAPISomministrazioni.md)
 - [DTOAPIUnitaMisura](docs/DTOAPIUnitaMisura.md)
 - [DTOAPIUser](docs/DTOAPIUser.md)
 - [DTOAPIVisita](docs/DTOAPIVisita.md)
 - [DTOAPIVisitaECG](docs/DTOAPIVisitaECG.md)
 - [DTOAPIVisitaPaziente](docs/DTOAPIVisitaPaziente.md)
 - [DTOAnamnesiFamiliare](docs/DTOAnamnesiFamiliare.md)
 - [DTOBisogniPazienteAlimentazione](docs/DTOBisogniPazienteAlimentazione.md)
 - [DTOBisogniPazienteComunicazione](docs/DTOBisogniPazienteComunicazione.md)
 - [DTOBisogniPazienteEliminazione](docs/DTOBisogniPazienteEliminazione.md)
 - [DTOBisogniPazienteIgiene](docs/DTOBisogniPazienteIgiene.md)
 - [DTOBisogniPazienteMobilizzazione](docs/DTOBisogniPazienteMobilizzazione.md)
 - [DTOBisogniPazienteSicurezzaSonno](docs/DTOBisogniPazienteSicurezzaSonno.md)
 - [DTODiarioClinico](docs/DTODiarioClinico.md)
 - [DTOEsameObiettivoGenerale](docs/DTOEsameObiettivoGenerale.md)
 - [DTOEsameObiettivoRegionale](docs/DTOEsameObiettivoRegionale.md)
 - [DTOEsameStrumentaleConclusioneTerapia](docs/DTOEsameStrumentaleConclusioneTerapia.md)
 - [DTOItemPrescrizione](docs/DTOItemPrescrizione.md)
 - [DTOItemPrestazioni](docs/DTOItemPrestazioni.md)
 - [DTOModelloParziale](docs/DTOModelloParziale.md)
 - [DTOPatologicaProssimaTerapieInAtto](docs/DTOPatologicaProssimaTerapieInAtto.md)
 - [DTOPatologicaProssimaUlcereDaPressione](docs/DTOPatologicaProssimaUlcereDaPressione.md)
 - [DTOPatologicaRemotaInterventiPregressi](docs/DTOPatologicaRemotaInterventiPregressi.md)
 - [DTOPatologicaRemotaMalattie](docs/DTOPatologicaRemotaMalattie.md)
 - [DTOPatologicaRemotaRicoveriPregressi](docs/DTOPatologicaRemotaRicoveriPregressi.md)
 - [DTOPrescrizione](docs/DTOPrescrizione.md)
 - [DTOPrestazione](docs/DTOPrestazione.md)
 - [DTOSVICAnagrafica](docs/DTOSVICAnagrafica.md)
 - [DTOSVICBudget](docs/DTOSVICBudget.md)
 - [DTOSVICDebitorePOST](docs/DTOSVICDebitorePOST.md)
 - [DTOSVICDebitorePOSTResult](docs/DTOSVICDebitorePOSTResult.md)
 - [DTOSVICMandatoGETResult](docs/DTOSVICMandatoGETResult.md)
 - [DTOSVICMandatoImpegnoPOST](docs/DTOSVICMandatoImpegnoPOST.md)
 - [DTOSVICMandatoPOSTResult](docs/DTOSVICMandatoPOSTResult.md)
 - [DTOSVICMandatoSpesaFissaPOST](docs/DTOSVICMandatoSpesaFissaPOST.md)
 - [DTOSVICMovimentazione](docs/DTOSVICMovimentazione.md)
 - [DTOSVICReversaleGETResult](docs/DTOSVICReversaleGETResult.md)
 - [DTOSVICReversalePOST](docs/DTOSVICReversalePOST.md)
 - [DTOSVICReversalePOSTResult](docs/DTOSVICReversalePOSTResult.md)
 - [DTOSVICRigaMandato](docs/DTOSVICRigaMandato.md)
 - [DTOSVICRigaReversale](docs/DTOSVICRigaReversale.md)
 - [DTOSomministrazione](docs/DTOSomministrazione.md)
 - [ExternalLoginViewModel](docs/ExternalLoginViewModel.md)
 - [ManageInfoViewModel](docs/ManageInfoViewModel.md)
 - [RegisterExternalBindingModel](docs/RegisterExternalBindingModel.md)
 - [RemoveLoginBindingModel](docs/RemoveLoginBindingModel.md)
 - [SetPasswordBindingModel](docs/SetPasswordBindingModel.md)
 - [UserInfoViewModel](docs/UserInfoViewModel.md)
 - [UserLoginInfoViewModel](docs/UserLoginInfoViewModel.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Bearer"></a>
### Bearer

- **Type**: HTTP basic authentication

<a id="apiKey"></a>
### apiKey

- **Type**: API key
- **API key parameter name**: apiKey
- **Location**: HTTP header


## Author




