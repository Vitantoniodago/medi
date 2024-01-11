# openapi_client.ArchivioParametriApi

All URIs are relative to *https://cloud.medihome.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archivio_parametri_check_prestazione**](ArchivioParametriApi.md#archivio_parametri_check_prestazione) | **POST** /api/ArchivioParametri/CheckPrestazione | Controllo della prestazione
[**archivio_parametri_crea_prestazione**](ArchivioParametriApi.md#archivio_parametri_crea_prestazione) | **POST** /api/ArchivioParametri/CreaPrestazione | Crea una prestazione.
[**archivio_parametri_interrompi_prestazione**](ArchivioParametriApi.md#archivio_parametri_interrompi_prestazione) | **POST** /api/ArchivioParametri/InterrompiPrestazione | Interrompi la prestazione.
[**archivio_parametri_invio_parametro**](ArchivioParametriApi.md#archivio_parametri_invio_parametro) | **POST** /api/ArchivioParametri/InvioParametro | Salvataggio di un parametro rilevato
[**archivio_parametri_invio_set_parametri**](ArchivioParametriApi.md#archivio_parametri_invio_set_parametri) | **POST** /api/ArchivioParametri/InvioSetParametri | Salvataggio di un set di parametri rilevato
[**archivio_parametri_parametri_rilevati**](ArchivioParametriApi.md#archivio_parametri_parametri_rilevati) | **POST** /api/ArchivioParametri/ParametriRilevati | Elenco dei parametri di un intervento.


# **archivio_parametri_check_prestazione**
> DTOAPIInterventoDomiciliare archivio_parametri_check_prestazione(intervento)

Controllo della prestazione

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_intervento_domiciliare import DTOAPIInterventoDomiciliare
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
    api_instance = openapi_client.ArchivioParametriApi(api_client)
    intervento = openapi_client.DTOAPIInterventoDomiciliare() # DTOAPIInterventoDomiciliare | Dettaglio di intervento con prestazione da controllare

    try:
        # Controllo della prestazione
        api_response = api_instance.archivio_parametri_check_prestazione(intervento)
        print("The response of ArchivioParametriApi->archivio_parametri_check_prestazione:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArchivioParametriApi->archivio_parametri_check_prestazione: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **intervento** | [**DTOAPIInterventoDomiciliare**](DTOAPIInterventoDomiciliare.md)| Dettaglio di intervento con prestazione da controllare | 

### Return type

[**DTOAPIInterventoDomiciliare**](DTOAPIInterventoDomiciliare.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archivio_parametri_crea_prestazione**
> DTOAPIInterventoDomiciliare archivio_parametri_crea_prestazione(session, user, intervento)

Crea una prestazione.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_intervento_domiciliare import DTOAPIInterventoDomiciliare
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
    api_instance = openapi_client.ArchivioParametriApi(api_client)
    session = 'session_example' # str | Sessione di accesso
    user = 'user_example' # str | Utente
    intervento = openapi_client.DTOAPIInterventoDomiciliare() # DTOAPIInterventoDomiciliare | Dettagli di intervento

    try:
        # Crea una prestazione.
        api_response = api_instance.archivio_parametri_crea_prestazione(session, user, intervento)
        print("The response of ArchivioParametriApi->archivio_parametri_crea_prestazione:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArchivioParametriApi->archivio_parametri_crea_prestazione: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session** | **str**| Sessione di accesso | 
 **user** | **str**| Utente | 
 **intervento** | [**DTOAPIInterventoDomiciliare**](DTOAPIInterventoDomiciliare.md)| Dettagli di intervento | 

### Return type

[**DTOAPIInterventoDomiciliare**](DTOAPIInterventoDomiciliare.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archivio_parametri_interrompi_prestazione**
> DTOAPIInterventoDomiciliare archivio_parametri_interrompi_prestazione(intervento)

Interrompi la prestazione.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_intervento_domiciliare import DTOAPIInterventoDomiciliare
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
    api_instance = openapi_client.ArchivioParametriApi(api_client)
    intervento = openapi_client.DTOAPIInterventoDomiciliare() # DTOAPIInterventoDomiciliare | Dettagli di intervento con prestazione da terminare

    try:
        # Interrompi la prestazione.
        api_response = api_instance.archivio_parametri_interrompi_prestazione(intervento)
        print("The response of ArchivioParametriApi->archivio_parametri_interrompi_prestazione:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArchivioParametriApi->archivio_parametri_interrompi_prestazione: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **intervento** | [**DTOAPIInterventoDomiciliare**](DTOAPIInterventoDomiciliare.md)| Dettagli di intervento con prestazione da terminare | 

### Return type

[**DTOAPIInterventoDomiciliare**](DTOAPIInterventoDomiciliare.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archivio_parametri_invio_parametro**
> bool archivio_parametri_invio_parametro(intervento)

Salvataggio di un parametro rilevato

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_parametro_prestazione import DTOAPIParametroPrestazione
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
    api_instance = openapi_client.ArchivioParametriApi(api_client)
    intervento = openapi_client.DTOAPIParametroPrestazione() # DTOAPIParametroPrestazione | Intervento per il quale si effettua la misurazione

    try:
        # Salvataggio di un parametro rilevato
        api_response = api_instance.archivio_parametri_invio_parametro(intervento)
        print("The response of ArchivioParametriApi->archivio_parametri_invio_parametro:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArchivioParametriApi->archivio_parametri_invio_parametro: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **intervento** | [**DTOAPIParametroPrestazione**](DTOAPIParametroPrestazione.md)| Intervento per il quale si effettua la misurazione | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archivio_parametri_invio_set_parametri**
> bool archivio_parametri_invio_set_parametri(interventi)

Salvataggio di un set di parametri rilevato

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_parametro_prestazione import DTOAPIParametroPrestazione
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
    api_instance = openapi_client.ArchivioParametriApi(api_client)
    interventi = [openapi_client.DTOAPIParametroPrestazione()] # List[DTOAPIParametroPrestazione] | Intervento per il quale si effettua la misurazione

    try:
        # Salvataggio di un set di parametri rilevato
        api_response = api_instance.archivio_parametri_invio_set_parametri(interventi)
        print("The response of ArchivioParametriApi->archivio_parametri_invio_set_parametri:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArchivioParametriApi->archivio_parametri_invio_set_parametri: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interventi** | [**List[DTOAPIParametroPrestazione]**](DTOAPIParametroPrestazione.md)| Intervento per il quale si effettua la misurazione | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archivio_parametri_parametri_rilevati**
> List[DTOAPIParametroPrestazione] archivio_parametri_parametri_rilevati(richiesta_parametri)

Elenco dei parametri di un intervento.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_parametro_prestazione import DTOAPIParametroPrestazione
from openapi_client.models.dtoapi_richiesta_parametri import DTOAPIRichiestaParametri
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
    api_instance = openapi_client.ArchivioParametriApi(api_client)
    richiesta_parametri = openapi_client.DTOAPIRichiestaParametri() # DTOAPIRichiestaParametri | Dettaglio di richiesta dei parametri

    try:
        # Elenco dei parametri di un intervento.
        api_response = api_instance.archivio_parametri_parametri_rilevati(richiesta_parametri)
        print("The response of ArchivioParametriApi->archivio_parametri_parametri_rilevati:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArchivioParametriApi->archivio_parametri_parametri_rilevati: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **richiesta_parametri** | [**DTOAPIRichiestaParametri**](DTOAPIRichiestaParametri.md)| Dettaglio di richiesta dei parametri | 

### Return type

[**List[DTOAPIParametroPrestazione]**](DTOAPIParametroPrestazione.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

