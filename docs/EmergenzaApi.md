# openapi_client.EmergenzaApi

All URIs are relative to *https://cloud.medihome.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emergenza_crea_visita**](EmergenzaApi.md#emergenza_crea_visita) | **POST** /api/Emergenza/CreaVisita | 


# **emergenza_crea_visita**
> DTOAPIVisita emergenza_crea_visita(emergenza)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_visita import DTOAPIVisita
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
    api_instance = openapi_client.EmergenzaApi(api_client)
    emergenza = openapi_client.DTOAPIVisita() # DTOAPIVisita | 

    try:
        api_response = api_instance.emergenza_crea_visita(emergenza)
        print("The response of EmergenzaApi->emergenza_crea_visita:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmergenzaApi->emergenza_crea_visita: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emergenza** | [**DTOAPIVisita**](DTOAPIVisita.md)|  | 

### Return type

[**DTOAPIVisita**](DTOAPIVisita.md)

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

