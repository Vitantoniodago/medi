# DTOPatologicaRemotaInterventiPregressi



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nega_intervento** | **bool** | Richiedi o modifica un valore che indica [nega intervento]. | [optional] 
**intervento** | **str** | Richiedi o modifica intervento. | [optional] 
**data_intervento** | **datetime** | Richiedi o modifica data intervento. | [optional] 
**eta** | **float** | Richiedi o modifica eta. | [optional] 
**patologia** | **str** | Richiedi o modifica patologia. | [optional] 
**note** | **str** | Richiedi o modifica note. | [optional] 
**id_patologica_remota_interventi_pregressi** | **int** | Richiedi o modifica identifier patologica remota interventi pregressi. | [optional] 
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**id_visita** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dto_patologica_remota_interventi_pregressi import DTOPatologicaRemotaInterventiPregressi

# TODO update the JSON string below
json = "{}"
# create an instance of DTOPatologicaRemotaInterventiPregressi from a JSON string
dto_patologica_remota_interventi_pregressi_instance = DTOPatologicaRemotaInterventiPregressi.from_json(json)
# print the JSON string representation of the object
print DTOPatologicaRemotaInterventiPregressi.to_json()

# convert the object into a dict
dto_patologica_remota_interventi_pregressi_dict = dto_patologica_remota_interventi_pregressi_instance.to_dict()
# create an instance of DTOPatologicaRemotaInterventiPregressi from a dict
dto_patologica_remota_interventi_pregressi_form_dict = dto_patologica_remota_interventi_pregressi.from_dict(dto_patologica_remota_interventi_pregressi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


