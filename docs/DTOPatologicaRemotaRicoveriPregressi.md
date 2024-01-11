# DTOPatologicaRemotaRicoveriPregressi



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_ricovero** | **datetime** | Richiedi o modifica data ricovero. | [optional] 
**unita_ospedaliera** | **str** | Richiedi o modifica unita ospedaliera. | [optional] 
**ospedale** | **str** | Richiedi o modifica ospedale. | [optional] 
**id_patologica_remota_ricoveri_pregressi** | **int** | Richiedi o modifica identifier patologica remota ricoveri pregressi. | [optional] 
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**id_visita** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dto_patologica_remota_ricoveri_pregressi import DTOPatologicaRemotaRicoveriPregressi

# TODO update the JSON string below
json = "{}"
# create an instance of DTOPatologicaRemotaRicoveriPregressi from a JSON string
dto_patologica_remota_ricoveri_pregressi_instance = DTOPatologicaRemotaRicoveriPregressi.from_json(json)
# print the JSON string representation of the object
print DTOPatologicaRemotaRicoveriPregressi.to_json()

# convert the object into a dict
dto_patologica_remota_ricoveri_pregressi_dict = dto_patologica_remota_ricoveri_pregressi_instance.to_dict()
# create an instance of DTOPatologicaRemotaRicoveriPregressi from a dict
dto_patologica_remota_ricoveri_pregressi_form_dict = dto_patologica_remota_ricoveri_pregressi.from_dict(dto_patologica_remota_ricoveri_pregressi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


