# openapi_client.SVICApi

All URIs are relative to *https://cloud.medihome.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**s_vic_budget**](SVICApi.md#s_vic_budget) | **POST** /api/SVIC/Budget | 
[**s_vic_debitore**](SVICApi.md#s_vic_debitore) | **POST** /api/finanziaria/debitore | 
[**s_vic_get_anagrafica**](SVICApi.md#s_vic_get_anagrafica) | **GET** /api/finanziaria/anagrafica | 
[**s_vic_mandato**](SVICApi.md#s_vic_mandato) | **GET** /api/finanziaria/mandato | 
[**s_vic_mandato_da_impegno**](SVICApi.md#s_vic_mandato_da_impegno) | **POST** /api/finanziaria/mandatodaimpegno | 
[**s_vic_mandato_spesa_fissa**](SVICApi.md#s_vic_mandato_spesa_fissa) | **POST** /api/finanziaria/mandatospesafissa | 
[**s_vic_movimentazione**](SVICApi.md#s_vic_movimentazione) | **POST** /api/SVIC/Movimentazione | 
[**s_vic_reversale**](SVICApi.md#s_vic_reversale) | **POST** /api/finanziaria/reversale | 
[**s_vic_reversale1**](SVICApi.md#s_vic_reversale1) | **GET** /api/finanziaria/reversale | 
[**s_vic_set_anagrafica**](SVICApi.md#s_vic_set_anagrafica) | **POST** /api/finanziaria/anagrafica | 


# **s_vic_budget**
> DTOSVICBudget s_vic_budget(budget)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtosvic_budget import DTOSVICBudget
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
    api_instance = openapi_client.SVICApi(api_client)
    budget = openapi_client.DTOSVICBudget() # DTOSVICBudget | 

    try:
        api_response = api_instance.s_vic_budget(budget)
        print("The response of SVICApi->s_vic_budget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SVICApi->s_vic_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget** | [**DTOSVICBudget**](DTOSVICBudget.md)|  | 

### Return type

[**DTOSVICBudget**](DTOSVICBudget.md)

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

# **s_vic_debitore**
> DTOSVICDebitorePOSTResult s_vic_debitore(debitore)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtosvic_debitore_post import DTOSVICDebitorePOST
from openapi_client.models.dtosvic_debitore_post_result import DTOSVICDebitorePOSTResult
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
    api_instance = openapi_client.SVICApi(api_client)
    debitore = openapi_client.DTOSVICDebitorePOST() # DTOSVICDebitorePOST | 

    try:
        api_response = api_instance.s_vic_debitore(debitore)
        print("The response of SVICApi->s_vic_debitore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SVICApi->s_vic_debitore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **debitore** | [**DTOSVICDebitorePOST**](DTOSVICDebitorePOST.md)|  | 

### Return type

[**DTOSVICDebitorePOSTResult**](DTOSVICDebitorePOSTResult.md)

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

# **s_vic_get_anagrafica**
> DTOSVICAnagrafica s_vic_get_anagrafica(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtosvic_anagrafica import DTOSVICAnagrafica
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
    api_instance = openapi_client.SVICApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.s_vic_get_anagrafica(id)
        print("The response of SVICApi->s_vic_get_anagrafica:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SVICApi->s_vic_get_anagrafica: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**DTOSVICAnagrafica**](DTOSVICAnagrafica.md)

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

# **s_vic_mandato**
> DTOSVICMandatoGETResult s_vic_mandato(anno, numero)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtosvic_mandato_get_result import DTOSVICMandatoGETResult
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
    api_instance = openapi_client.SVICApi(api_client)
    anno = 56 # int | 
    numero = 56 # int | 

    try:
        api_response = api_instance.s_vic_mandato(anno, numero)
        print("The response of SVICApi->s_vic_mandato:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SVICApi->s_vic_mandato: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anno** | **int**|  | 
 **numero** | **int**|  | 

### Return type

[**DTOSVICMandatoGETResult**](DTOSVICMandatoGETResult.md)

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

# **s_vic_mandato_da_impegno**
> DTOSVICMandatoPOSTResult s_vic_mandato_da_impegno(mandato)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtosvic_mandato_impegno_post import DTOSVICMandatoImpegnoPOST
from openapi_client.models.dtosvic_mandato_post_result import DTOSVICMandatoPOSTResult
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
    api_instance = openapi_client.SVICApi(api_client)
    mandato = openapi_client.DTOSVICMandatoImpegnoPOST() # DTOSVICMandatoImpegnoPOST | 

    try:
        api_response = api_instance.s_vic_mandato_da_impegno(mandato)
        print("The response of SVICApi->s_vic_mandato_da_impegno:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SVICApi->s_vic_mandato_da_impegno: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mandato** | [**DTOSVICMandatoImpegnoPOST**](DTOSVICMandatoImpegnoPOST.md)|  | 

### Return type

[**DTOSVICMandatoPOSTResult**](DTOSVICMandatoPOSTResult.md)

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

# **s_vic_mandato_spesa_fissa**
> DTOSVICMandatoPOSTResult s_vic_mandato_spesa_fissa(mandato)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtosvic_mandato_post_result import DTOSVICMandatoPOSTResult
from openapi_client.models.dtosvic_mandato_spesa_fissa_post import DTOSVICMandatoSpesaFissaPOST
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
    api_instance = openapi_client.SVICApi(api_client)
    mandato = openapi_client.DTOSVICMandatoSpesaFissaPOST() # DTOSVICMandatoSpesaFissaPOST | 

    try:
        api_response = api_instance.s_vic_mandato_spesa_fissa(mandato)
        print("The response of SVICApi->s_vic_mandato_spesa_fissa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SVICApi->s_vic_mandato_spesa_fissa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mandato** | [**DTOSVICMandatoSpesaFissaPOST**](DTOSVICMandatoSpesaFissaPOST.md)|  | 

### Return type

[**DTOSVICMandatoPOSTResult**](DTOSVICMandatoPOSTResult.md)

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

# **s_vic_movimentazione**
> DTOSVICMovimentazione s_vic_movimentazione(movimento)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtosvic_movimentazione import DTOSVICMovimentazione
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
    api_instance = openapi_client.SVICApi(api_client)
    movimento = openapi_client.DTOSVICMovimentazione() # DTOSVICMovimentazione | 

    try:
        api_response = api_instance.s_vic_movimentazione(movimento)
        print("The response of SVICApi->s_vic_movimentazione:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SVICApi->s_vic_movimentazione: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movimento** | [**DTOSVICMovimentazione**](DTOSVICMovimentazione.md)|  | 

### Return type

[**DTOSVICMovimentazione**](DTOSVICMovimentazione.md)

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

# **s_vic_reversale**
> DTOSVICReversalePOSTResult s_vic_reversale(reversale)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtosvic_reversale_post import DTOSVICReversalePOST
from openapi_client.models.dtosvic_reversale_post_result import DTOSVICReversalePOSTResult
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
    api_instance = openapi_client.SVICApi(api_client)
    reversale = openapi_client.DTOSVICReversalePOST() # DTOSVICReversalePOST | 

    try:
        api_response = api_instance.s_vic_reversale(reversale)
        print("The response of SVICApi->s_vic_reversale:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SVICApi->s_vic_reversale: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reversale** | [**DTOSVICReversalePOST**](DTOSVICReversalePOST.md)|  | 

### Return type

[**DTOSVICReversalePOSTResult**](DTOSVICReversalePOSTResult.md)

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

# **s_vic_reversale1**
> DTOSVICReversaleGETResult s_vic_reversale1(anno, numero)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtosvic_reversale_get_result import DTOSVICReversaleGETResult
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
    api_instance = openapi_client.SVICApi(api_client)
    anno = 56 # int | 
    numero = 56 # int | 

    try:
        api_response = api_instance.s_vic_reversale1(anno, numero)
        print("The response of SVICApi->s_vic_reversale1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SVICApi->s_vic_reversale1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anno** | **int**|  | 
 **numero** | **int**|  | 

### Return type

[**DTOSVICReversaleGETResult**](DTOSVICReversaleGETResult.md)

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

# **s_vic_set_anagrafica**
> str s_vic_set_anagrafica(anagrafica)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtosvic_anagrafica import DTOSVICAnagrafica
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
    api_instance = openapi_client.SVICApi(api_client)
    anagrafica = openapi_client.DTOSVICAnagrafica() # DTOSVICAnagrafica | 

    try:
        api_response = api_instance.s_vic_set_anagrafica(anagrafica)
        print("The response of SVICApi->s_vic_set_anagrafica:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SVICApi->s_vic_set_anagrafica: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anagrafica** | [**DTOSVICAnagrafica**](DTOSVICAnagrafica.md)|  | 

### Return type

**str**

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

