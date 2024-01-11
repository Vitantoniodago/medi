# DTOAPIPrestazione



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_prestazione_pai** | **int** | Richiedi o modifica identifier prestazione pai. | [optional] 
**id_prestazione** | **int** | Richiedi o modifica identifier prestazione. | [optional] 
**prestazione** | **str** | Richiedi o modifica prestazione. | [optional] 
**descrizione** | **str** | Richiedi o modifica descrizione. | [optional] 
**durata** | **float** | Richiedi o modifica durata. | [optional] 

## Example

```python
from openapi_client.models.dtoapi_prestazione import DTOAPIPrestazione

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIPrestazione from a JSON string
dtoapi_prestazione_instance = DTOAPIPrestazione.from_json(json)
# print the JSON string representation of the object
print DTOAPIPrestazione.to_json()

# convert the object into a dict
dtoapi_prestazione_dict = dtoapi_prestazione_instance.to_dict()
# create an instance of DTOAPIPrestazione from a dict
dtoapi_prestazione_form_dict = dtoapi_prestazione.from_dict(dtoapi_prestazione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


