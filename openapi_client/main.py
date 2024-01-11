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
    api_instance = openapi_client.SomministrazioneApi(api_client)
    model = openapi_client.DTOSomministrazione() # DTOSomministrazione | Modello di dati per login esterna

    try:
        # Aggiunta di una servizio di login esterno
        api_response = api_instance.somministrazione_planning(model)
        print("The response of AccountApi->account_add_external_login:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->account_add_external_login: %s\n" % e)