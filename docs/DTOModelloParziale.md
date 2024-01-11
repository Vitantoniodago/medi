# DTOModelloParziale



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_start** | **datetime** | Richiedi o modifica time start. | [optional] 
**time_end** | **datetime** | Richiedi o modifica time end. | [optional] 
**settimana** | **List[bool]** | Richiedi o modifica settimana. | [optional] 
**gg_settimana** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dto_modello_parziale import DTOModelloParziale

# TODO update the JSON string below
json = "{}"
# create an instance of DTOModelloParziale from a JSON string
dto_modello_parziale_instance = DTOModelloParziale.from_json(json)
# print the JSON string representation of the object
print DTOModelloParziale.to_json()

# convert the object into a dict
dto_modello_parziale_dict = dto_modello_parziale_instance.to_dict()
# create an instance of DTOModelloParziale from a dict
dto_modello_parziale_form_dict = dto_modello_parziale.from_dict(dto_modello_parziale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


