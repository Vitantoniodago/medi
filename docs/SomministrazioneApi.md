# openapi_client.SomministrazioneApi

All URIs are relative to *https://cloud.medihome.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**somministrazione_planning**](SomministrazioneApi.md#somministrazione_planning) | **POST** /api/Somministrazione/Planning | 


# **somministrazione_planning**
> DTOAPISomministrazioni somministrazione_planning(richiesta)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_richiesta_somministrazioni import DTOAPIRichiestaSomministrazioni
from openapi_client.models.dtoapi_somministrazioni import DTOAPISomministrazioni
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
    api_instance = openapi_client.SomministrazioneApi(api_client)
    richiesta = openapi_client.DTOAPIRichiestaSomministrazioni() # DTOAPIRichiestaSomministrazioni | 

    try:
        api_response = api_instance.somministrazione_planning(richiesta)
        print("The response of SomministrazioneApi->somministrazione_planning:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SomministrazioneApi->somministrazione_planning: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **richiesta** | [**DTOAPIRichiestaSomministrazioni**](DTOAPIRichiestaSomministrazioni.md)|  | 

### Return type

[**DTOAPISomministrazioni**](DTOAPISomministrazioni.md)

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

