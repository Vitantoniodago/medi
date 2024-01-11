# openapi_client.DeviceApi

All URIs are relative to *https://cloud.medihome.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_licenza**](DeviceApi.md#device_licenza) | **POST** /api/Device/Licenza | 


# **device_licenza**
> DTOAPIDevice device_licenza(device)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_device import DTOAPIDevice
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
    api_instance = openapi_client.DeviceApi(api_client)
    device = openapi_client.DTOAPIDevice() # DTOAPIDevice | 

    try:
        api_response = api_instance.device_licenza(device)
        print("The response of DeviceApi->device_licenza:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->device_licenza: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**DTOAPIDevice**](DTOAPIDevice.md)|  | 

### Return type

[**DTOAPIDevice**](DTOAPIDevice.md)

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

