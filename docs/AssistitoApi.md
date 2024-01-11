# openapi_client.AssistitoApi

All URIs are relative to *https://cloud.medihome.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assistito_lista**](AssistitoApi.md#assistito_lista) | **POST** /api/Assistito/Lista | 
[**assistito_scheda**](AssistitoApi.md#assistito_scheda) | **POST** /api/Assistito/Scheda | 
[**assistito_somministrazioni**](AssistitoApi.md#assistito_somministrazioni) | **POST** /api/Assistito/Somministrazioni | 


# **assistito_lista**
> List[DTOAPIAssistito] assistito_lista(session)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_assistito import DTOAPIAssistito
from openapi_client.models.dtoapi_session import DTOAPISession
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
    api_instance = openapi_client.AssistitoApi(api_client)
    session = openapi_client.DTOAPISession() # DTOAPISession | 

    try:
        api_response = api_instance.assistito_lista(session)
        print("The response of AssistitoApi->assistito_lista:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssistitoApi->assistito_lista: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session** | [**DTOAPISession**](DTOAPISession.md)|  | 

### Return type

[**List[DTOAPIAssistito]**](DTOAPIAssistito.md)

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

# **assistito_scheda**
> object assistito_scheda(assistito)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_assistito import DTOAPIAssistito
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
    api_instance = openapi_client.AssistitoApi(api_client)
    assistito = openapi_client.DTOAPIAssistito() # DTOAPIAssistito | 

    try:
        api_response = api_instance.assistito_scheda(assistito)
        print("The response of AssistitoApi->assistito_scheda:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssistitoApi->assistito_scheda: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assistito** | [**DTOAPIAssistito**](DTOAPIAssistito.md)|  | 

### Return type

**object**

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

# **assistito_somministrazioni**
> object assistito_somministrazioni(assistito)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_assistito import DTOAPIAssistito
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
    api_instance = openapi_client.AssistitoApi(api_client)
    assistito = openapi_client.DTOAPIAssistito() # DTOAPIAssistito | 

    try:
        api_response = api_instance.assistito_somministrazioni(assistito)
        print("The response of AssistitoApi->assistito_somministrazioni:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssistitoApi->assistito_somministrazioni: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assistito** | [**DTOAPIAssistito**](DTOAPIAssistito.md)|  | 

### Return type

**object**

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

