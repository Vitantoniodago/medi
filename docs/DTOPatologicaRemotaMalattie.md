# DTOPatologicaRemotaMalattie



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diagnosi** | **str** | Richiedi o modifica diagnosi. | [optional] 
**id_stato_malattia** | **int** | Richiedi o modifica identifier stato malattia. | [optional] 
**eta_malattia** | **float** | Richiedi o modifica eta malattia. | [optional] 
**note** | **str** | Richiedi o modifica note. | [optional] 
**id_patologica_remota_malattie** | **int** | Richiedi o modifica identifier patologica remota malattie. | [optional] 
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**id_visita** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dto_patologica_remota_malattie import DTOPatologicaRemotaMalattie

# TODO update the JSON string below
json = "{}"
# create an instance of DTOPatologicaRemotaMalattie from a JSON string
dto_patologica_remota_malattie_instance = DTOPatologicaRemotaMalattie.from_json(json)
# print the JSON string representation of the object
print DTOPatologicaRemotaMalattie.to_json()

# convert the object into a dict
dto_patologica_remota_malattie_dict = dto_patologica_remota_malattie_instance.to_dict()
# create an instance of DTOPatologicaRemotaMalattie from a dict
dto_patologica_remota_malattie_form_dict = dto_patologica_remota_malattie.from_dict(dto_patologica_remota_malattie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


