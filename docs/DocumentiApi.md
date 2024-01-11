# openapi_client.DocumentiApi

All URIs are relative to *https://cloud.medihome.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documenti_fattura**](DocumentiApi.md#documenti_fattura) | **POST** /api/Documenti/Fattura | 
[**documenti_fatture**](DocumentiApi.md#documenti_fatture) | **POST** /api/Documenti/Fatture | 


# **documenti_fattura**
> DTOAPIFattura documenti_fattura(documento)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_documento import DTOAPIDocumento
from openapi_client.models.dtoapi_fattura import DTOAPIFattura
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
    api_instance = openapi_client.DocumentiApi(api_client)
    documento = openapi_client.DTOAPIDocumento() # DTOAPIDocumento | 

    try:
        api_response = api_instance.documenti_fattura(documento)
        print("The response of DocumentiApi->documenti_fattura:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentiApi->documenti_fattura: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documento** | [**DTOAPIDocumento**](DTOAPIDocumento.md)|  | 

### Return type

[**DTOAPIFattura**](DTOAPIFattura.md)

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

# **documenti_fatture**
> List[DTOAPIFattura] documenti_fatture(filtro)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_fattura import DTOAPIFattura
from openapi_client.models.dtoapi_filtri_documento import DTOAPIFiltriDocumento
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
    api_instance = openapi_client.DocumentiApi(api_client)
    filtro = openapi_client.DTOAPIFiltriDocumento() # DTOAPIFiltriDocumento | 

    try:
        api_response = api_instance.documenti_fatture(filtro)
        print("The response of DocumentiApi->documenti_fatture:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentiApi->documenti_fatture: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filtro** | [**DTOAPIFiltriDocumento**](DTOAPIFiltriDocumento.md)|  | 

### Return type

[**List[DTOAPIFattura]**](DTOAPIFattura.md)

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

