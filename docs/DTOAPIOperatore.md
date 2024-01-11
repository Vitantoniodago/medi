# DTOAPIOperatore



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_operatore** | **int** | Richiedi o modifica identifier operatore. | [optional] 
**nome** | **str** | Richiedi o modifica nome. | [optional] 
**cognome** | **str** | Richiedi o modifica cognome. | [optional] 

## Example

```python
from openapi_client.models.dtoapi_operatore import DTOAPIOperatore

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIOperatore from a JSON string
dtoapi_operatore_instance = DTOAPIOperatore.from_json(json)
# print the JSON string representation of the object
print DTOAPIOperatore.to_json()

# convert the object into a dict
dtoapi_operatore_dict = dtoapi_operatore_instance.to_dict()
# create an instance of DTOAPIOperatore from a dict
dtoapi_operatore_form_dict = dtoapi_operatore.from_dict(dtoapi_operatore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


