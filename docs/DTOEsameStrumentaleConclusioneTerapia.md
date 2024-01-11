# DTOEsameStrumentaleConclusioneTerapia



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_conclusione_terapia** | **int** | Richiedi o modifica identifier conclusione terapia. | [optional] 
**id_assistito** | **int** |  | [optional] 
**note_conclusioni** | **str** | Richiedi o modifica note conclusioni. | [optional] 
**conclusioni** | **str** | Richiedi o modifica conclusioni. | [optional] 
**consigli_terapia** | **str** | Richiedi o modifica consigli terapia. | [optional] 
**id_referto** | **int** |  | [optional] 
**id_visita** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dto_esame_strumentale_conclusione_terapia import DTOEsameStrumentaleConclusioneTerapia

# TODO update the JSON string below
json = "{}"
# create an instance of DTOEsameStrumentaleConclusioneTerapia from a JSON string
dto_esame_strumentale_conclusione_terapia_instance = DTOEsameStrumentaleConclusioneTerapia.from_json(json)
# print the JSON string representation of the object
print DTOEsameStrumentaleConclusioneTerapia.to_json()

# convert the object into a dict
dto_esame_strumentale_conclusione_terapia_dict = dto_esame_strumentale_conclusione_terapia_instance.to_dict()
# create an instance of DTOEsameStrumentaleConclusioneTerapia from a dict
dto_esame_strumentale_conclusione_terapia_form_dict = dto_esame_strumentale_conclusione_terapia.from_dict(dto_esame_strumentale_conclusione_terapia_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


