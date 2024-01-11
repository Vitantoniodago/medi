# DTODiarioClinico



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valido_da** | **datetime** | Richiedi o modifica valido da. | [optional] 
**valido_a** | **datetime** | Richiedi o modifica valido a. | [optional] 
**note** | **str** | Richiedi o modifica note. | [optional] 
**id_diario_clinico** | **int** | Richiedi o modifica identifier diario clinico. | [optional] 
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**id_visita** | **int** |  | [optional] 
**priorita** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dto_diario_clinico import DTODiarioClinico

# TODO update the JSON string below
json = "{}"
# create an instance of DTODiarioClinico from a JSON string
dto_diario_clinico_instance = DTODiarioClinico.from_json(json)
# print the JSON string representation of the object
print DTODiarioClinico.to_json()

# convert the object into a dict
dto_diario_clinico_dict = dto_diario_clinico_instance.to_dict()
# create an instance of DTODiarioClinico from a dict
dto_diario_clinico_form_dict = dto_diario_clinico.from_dict(dto_diario_clinico_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


