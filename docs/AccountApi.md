# openapi_client.AccountApi

All URIs are relative to *https://cloud.medihome.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_add_external_login**](AccountApi.md#account_add_external_login) | **POST** /api/Account/AddExternalLogin | Aggiunta di una servizio di login esterno
[**account_change_password**](AccountApi.md#account_change_password) | **POST** /api/Account/ChangePassword | Cambia la password utente
[**account_get_external_login**](AccountApi.md#account_get_external_login) | **GET** /api/Account/ExternalLogin | Accesso tramite provider di terze parti
[**account_get_external_logins**](AccountApi.md#account_get_external_logins) | **GET** /api/Account/ExternalLogins | Accesso tramite provider di terze parti
[**account_get_manage_info**](AccountApi.md#account_get_manage_info) | **GET** /api/Account/ManageInfo | Restituisce le informazioni di managment dell&#39;utente
[**account_get_user_info**](AccountApi.md#account_get_user_info) | **GET** /api/Account/UserInfo | Restituisce le informazioni dell&#39;utente
[**account_login**](AccountApi.md#account_login) | **POST** /api/Account/Session | Login di uno specifico utente
[**account_logout**](AccountApi.md#account_logout) | **POST** /api/Account/Logout | Disconnetti istanza
[**account_register**](AccountApi.md#account_register) | **POST** /api/Account/Register | Registra un nuovo utente per l&#39;accesso al sistema
[**account_register_external**](AccountApi.md#account_register_external) | **POST** /api/Account/RegisterExternal | Registers the external.
[**account_remove_login**](AccountApi.md#account_remove_login) | **POST** /api/Account/RemoveLogin | Rimuovere una login esterna
[**account_set_password**](AccountApi.md#account_set_password) | **POST** /api/Account/SetPassword | Imposta la password


# **account_add_external_login**
> object account_add_external_login(model)

Aggiunta di una servizio di login esterno

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.add_external_login_binding_model import AddExternalLoginBindingModel
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
    except Exception as e:
        print("Exception when calling AccountApi->account_add_external_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**AddExternalLoginBindingModel**](AddExternalLoginBindingModel.md)| Modello di dati per login esterna | 

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

# **account_change_password**
> object account_change_password(model)

Cambia la password utente

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.change_password_binding_model import ChangePasswordBindingModel
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
    model = openapi_client.ChangePasswordBindingModel() # ChangePasswordBindingModel | Informazioni utente per il cambio password

    try:
        # Cambia la password utente
        api_response = api_instance.account_change_password(model)
        print("The response of AccountApi->account_change_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**ChangePasswordBindingModel**](ChangePasswordBindingModel.md)| Informazioni utente per il cambio password | 

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

# **account_get_external_login**
> object account_get_external_login(provider, error=error)

Accesso tramite provider di terze parti

### Example


```python
import time
import os
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
    provider = 'provider_example' # str | Provider di autenticazione
    error = 'error_example' # str | Errore (optional)

    try:
        # Accesso tramite provider di terze parti
        api_response = api_instance.account_get_external_login(provider, error=error)
        print("The response of AccountApi->account_get_external_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_get_external_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| Provider di autenticazione | 
 **error** | **str**| Errore | [optional] 

### Return type

**object**

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

# **account_get_external_logins**
> List[ExternalLoginViewModel] account_get_external_logins(return_url, generate_state=generate_state)

Accesso tramite provider di terze parti

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.external_login_view_model import ExternalLoginViewModel
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
    return_url = 'return_url_example' # str | Url di ritorno
    generate_state = True # bool | Settato a true [generate state]. (optional)

    try:
        # Accesso tramite provider di terze parti
        api_response = api_instance.account_get_external_logins(return_url, generate_state=generate_state)
        print("The response of AccountApi->account_get_external_logins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_get_external_logins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_url** | **str**| Url di ritorno | 
 **generate_state** | **bool**| Settato a true [generate state]. | [optional] 

### Return type

[**List[ExternalLoginViewModel]**](ExternalLoginViewModel.md)

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

# **account_get_manage_info**
> ManageInfoViewModel account_get_manage_info(return_url, generate_state=generate_state)

Restituisce le informazioni di managment dell'utente

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.manage_info_view_model import ManageInfoViewModel
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
    return_url = 'return_url_example' # str | Url di ritorno
    generate_state = True # bool | Se settato vero [generate state]. (optional)

    try:
        # Restituisce le informazioni di managment dell'utente
        api_response = api_instance.account_get_manage_info(return_url, generate_state=generate_state)
        print("The response of AccountApi->account_get_manage_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_get_manage_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_url** | **str**| Url di ritorno | 
 **generate_state** | **bool**| Se settato vero [generate state]. | [optional] 

### Return type

[**ManageInfoViewModel**](ManageInfoViewModel.md)

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

# **account_get_user_info**
> UserInfoViewModel account_get_user_info()

Restituisce le informazioni dell'utente

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.user_info_view_model import UserInfoViewModel
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

    try:
        # Restituisce le informazioni dell'utente
        api_response = api_instance.account_get_user_info()
        print("The response of AccountApi->account_get_user_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_get_user_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserInfoViewModel**](UserInfoViewModel.md)

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

# **account_login**
> DTOAPISession account_login(user_login)

Login di uno specifico utente

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_session import DTOAPISession
from openapi_client.models.dtoapi_user import DTOAPIUser
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
    user_login = openapi_client.DTOAPIUser() # DTOAPIUser | Informazioni login utente

    try:
        # Login di uno specifico utente
        api_response = api_instance.account_login(user_login)
        print("The response of AccountApi->account_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_login** | [**DTOAPIUser**](DTOAPIUser.md)| Informazioni login utente | 

### Return type

[**DTOAPISession**](DTOAPISession.md)

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

# **account_logout**
> object account_logout()

Disconnetti istanza

### Example


```python
import time
import os
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

    try:
        # Disconnetti istanza
        api_response = api_instance.account_logout()
        print("The response of AccountApi->account_logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_logout: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **account_register**
> DTOAPISession account_register(user_register)

Registra un nuovo utente per l'accesso al sistema

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dtoapi_session import DTOAPISession
from openapi_client.models.dtoapi_user import DTOAPIUser
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
    user_register = openapi_client.DTOAPIUser() # DTOAPIUser | Informazioni utente registrato

    try:
        # Registra un nuovo utente per l'accesso al sistema
        api_response = api_instance.account_register(user_register)
        print("The response of AccountApi->account_register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_register** | [**DTOAPIUser**](DTOAPIUser.md)| Informazioni utente registrato | 

### Return type

[**DTOAPISession**](DTOAPISession.md)

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

# **account_register_external**
> object account_register_external(model)

Registers the external.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.register_external_binding_model import RegisterExternalBindingModel
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
    model = openapi_client.RegisterExternalBindingModel() # RegisterExternalBindingModel | The model.

    try:
        # Registers the external.
        api_response = api_instance.account_register_external(model)
        print("The response of AccountApi->account_register_external:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_register_external: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**RegisterExternalBindingModel**](RegisterExternalBindingModel.md)| The model. | 

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

# **account_remove_login**
> object account_remove_login(model)

Rimuovere una login esterna

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.remove_login_binding_model import RemoveLoginBindingModel
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
    model = openapi_client.RemoveLoginBindingModel() # RemoveLoginBindingModel | Modello di dati per la rimozione dell'accesso

    try:
        # Rimuovere una login esterna
        api_response = api_instance.account_remove_login(model)
        print("The response of AccountApi->account_remove_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_remove_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**RemoveLoginBindingModel**](RemoveLoginBindingModel.md)| Modello di dati per la rimozione dell&#39;accesso | 

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

# **account_set_password**
> object account_set_password(model)

Imposta la password

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.set_password_binding_model import SetPasswordBindingModel
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
    model = openapi_client.SetPasswordBindingModel() # SetPasswordBindingModel | Modello di gestione password

    try:
        # Imposta la password
        api_response = api_instance.account_set_password(model)
        print("The response of AccountApi->account_set_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_set_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**SetPasswordBindingModel**](SetPasswordBindingModel.md)| Modello di gestione password | 

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

