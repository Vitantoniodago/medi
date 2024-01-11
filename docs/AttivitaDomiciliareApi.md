# openapi_client.AttivitaDomiciliareApi

All URIs are relative to *https://cloud.medihome.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attivita_domiciliare_interventi**](AttivitaDomiciliareApi.md#attivita_domiciliare_interventi) | **POST** /api/AttivitaDomiciliare/Interventi | Lista degli interventi con richiesta parametrizzata
[**attivita_domiciliare_interventi1**](AttivitaDomiciliareApi.md#attivita_domiciliare_interventi1) | **GET** /api/AttivitaDomiciliare/Interventi/{id} | Lista degli interventi di un assistito
[**attivita_domiciliare_interventi_assistito**](AttivitaDomiciliareApi.md#attivita_domiciliare_interventi_assistito) | **POST** /api/AttivitaDomiciliare/InterventiAssistito | Lista degli interventi di un assistito con richiesta parametrizzata
[**attivita_domiciliare_prossimo_intervento**](AttivitaDomiciliareApi.md#attivita_domiciliare_prossimo_intervento) | **POST** /api/AttivitaDomiciliare/ProssimoIntervento | Prossimo intervento.
[**attivita_domiciliare_prossimo_intervento_assistito**](AttivitaDomiciliareApi.md#attivita_domiciliare_prossimo_intervento_assistito) | **POST** /api/AttivitaDomiciliare/ProssimoInterventoAssistito | Prossimo intervento di un assistito.


# **attivita_domiciliare_interventi**
> List[DTOAPIAttivitaEsterna] attivita_domiciliare_interventi(richiesta)

Lista degli interventi con richiesta parametrizzata

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_attivita_esterna import DTOAPIAttivitaEsterna
from openapi_client.models.dtoapi_richiesta_interventi import DTOAPIRichiestaInterventi
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
    api_instance = openapi_client.AttivitaDomiciliareApi(api_client)
    richiesta = openapi_client.DTOAPIRichiestaInterventi() # DTOAPIRichiestaInterventi | Richiesta parametrizzata per la ricerca dell'elenco

    try:
        # Lista degli interventi con richiesta parametrizzata
        api_response = api_instance.attivita_domiciliare_interventi(richiesta)
        print("The response of AttivitaDomiciliareApi->attivita_domiciliare_interventi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttivitaDomiciliareApi->attivita_domiciliare_interventi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **richiesta** | [**DTOAPIRichiestaInterventi**](DTOAPIRichiestaInterventi.md)| Richiesta parametrizzata per la ricerca dell&#39;elenco | 

### Return type

[**List[DTOAPIAttivitaEsterna]**](DTOAPIAttivitaEsterna.md)

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

# **attivita_domiciliare_interventi1**
> List[DTOAPIAttivitaEsterna] attivita_domiciliare_interventi1(id)

Lista degli interventi di un assistito

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_attivita_esterna import DTOAPIAttivitaEsterna
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
    api_instance = openapi_client.AttivitaDomiciliareApi(api_client)
    id = 56 # int | Identificato dell'assistito

    try:
        # Lista degli interventi di un assistito
        api_response = api_instance.attivita_domiciliare_interventi1(id)
        print("The response of AttivitaDomiciliareApi->attivita_domiciliare_interventi1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttivitaDomiciliareApi->attivita_domiciliare_interventi1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identificato dell&#39;assistito | 

### Return type

[**List[DTOAPIAttivitaEsterna]**](DTOAPIAttivitaEsterna.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attivita_domiciliare_interventi_assistito**
> List[DTOAPIAttivitaEsterna] attivita_domiciliare_interventi_assistito(richiesta)

Lista degli interventi di un assistito con richiesta parametrizzata

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_attivita_esterna import DTOAPIAttivitaEsterna
from openapi_client.models.dtoapi_richiesta_interventi import DTOAPIRichiestaInterventi
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
    api_instance = openapi_client.AttivitaDomiciliareApi(api_client)
    richiesta = openapi_client.DTOAPIRichiestaInterventi() # DTOAPIRichiestaInterventi | Richiesta parametrizzata per la ricerca dell'elenco

    try:
        # Lista degli interventi di un assistito con richiesta parametrizzata
        api_response = api_instance.attivita_domiciliare_interventi_assistito(richiesta)
        print("The response of AttivitaDomiciliareApi->attivita_domiciliare_interventi_assistito:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttivitaDomiciliareApi->attivita_domiciliare_interventi_assistito: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **richiesta** | [**DTOAPIRichiestaInterventi**](DTOAPIRichiestaInterventi.md)| Richiesta parametrizzata per la ricerca dell&#39;elenco | 

### Return type

[**List[DTOAPIAttivitaEsterna]**](DTOAPIAttivitaEsterna.md)

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

# **attivita_domiciliare_prossimo_intervento**
> DTOAPIAttivitaEsterna attivita_domiciliare_prossimo_intervento(richiesta)

Prossimo intervento.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_attivita_esterna import DTOAPIAttivitaEsterna
from openapi_client.models.dtoapi_richiesta_interventi import DTOAPIRichiestaInterventi
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
    api_instance = openapi_client.AttivitaDomiciliareApi(api_client)
    richiesta = openapi_client.DTOAPIRichiestaInterventi() # DTOAPIRichiestaInterventi | Richiesta parametrizzata per la ricerca dell'elenco

    try:
        # Prossimo intervento.
        api_response = api_instance.attivita_domiciliare_prossimo_intervento(richiesta)
        print("The response of AttivitaDomiciliareApi->attivita_domiciliare_prossimo_intervento:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttivitaDomiciliareApi->attivita_domiciliare_prossimo_intervento: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **richiesta** | [**DTOAPIRichiestaInterventi**](DTOAPIRichiestaInterventi.md)| Richiesta parametrizzata per la ricerca dell&#39;elenco | 

### Return type

[**DTOAPIAttivitaEsterna**](DTOAPIAttivitaEsterna.md)

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

# **attivita_domiciliare_prossimo_intervento_assistito**
> DTOAPIAttivitaEsterna attivita_domiciliare_prossimo_intervento_assistito(richiesta)

Prossimo intervento di un assistito.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_attivita_esterna import DTOAPIAttivitaEsterna
from openapi_client.models.dtoapi_richiesta_interventi import DTOAPIRichiestaInterventi
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
    api_instance = openapi_client.AttivitaDomiciliareApi(api_client)
    richiesta = openapi_client.DTOAPIRichiestaInterventi() # DTOAPIRichiestaInterventi | Richiesta parametrizzata per la ricerca dell'elenco

    try:
        # Prossimo intervento di un assistito.
        api_response = api_instance.attivita_domiciliare_prossimo_intervento_assistito(richiesta)
        print("The response of AttivitaDomiciliareApi->attivita_domiciliare_prossimo_intervento_assistito:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttivitaDomiciliareApi->attivita_domiciliare_prossimo_intervento_assistito: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **richiesta** | [**DTOAPIRichiestaInterventi**](DTOAPIRichiestaInterventi.md)| Richiesta parametrizzata per la ricerca dell&#39;elenco | 

### Return type

[**DTOAPIAttivitaEsterna**](DTOAPIAttivitaEsterna.md)

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

