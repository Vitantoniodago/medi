# DTOAPIBisogniPaziente



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bisogni_paziente_aliemntazione** | [**List[DTOBisogniPazienteAlimentazione]**](DTOBisogniPazienteAlimentazione.md) |  | [optional] 
**bisogni_paziente_comunicazione** | [**List[DTOBisogniPazienteComunicazione]**](DTOBisogniPazienteComunicazione.md) |  | [optional] 
**bisogni_paziente_eliminazione** | [**List[DTOBisogniPazienteEliminazione]**](DTOBisogniPazienteEliminazione.md) |  | [optional] 
**bisogni_paziente_igiene** | [**List[DTOBisogniPazienteIgiene]**](DTOBisogniPazienteIgiene.md) |  | [optional] 
**bisogni_paziente_mobilizzazione** | [**List[DTOBisogniPazienteMobilizzazione]**](DTOBisogniPazienteMobilizzazione.md) |  | [optional] 
**bisogni_paziente_sicurezza_sonno** | [**List[DTOBisogniPazienteSicurezzaSonno]**](DTOBisogniPazienteSicurezzaSonno.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_bisogni_paziente import DTOAPIBisogniPaziente

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIBisogniPaziente from a JSON string
dtoapi_bisogni_paziente_instance = DTOAPIBisogniPaziente.from_json(json)
# print the JSON string representation of the object
print DTOAPIBisogniPaziente.to_json()

# convert the object into a dict
dtoapi_bisogni_paziente_dict = dtoapi_bisogni_paziente_instance.to_dict()
# create an instance of DTOAPIBisogniPaziente from a dict
dtoapi_bisogni_paziente_form_dict = dtoapi_bisogni_paziente.from_dict(dtoapi_bisogni_paziente_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


