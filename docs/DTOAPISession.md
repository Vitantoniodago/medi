# DTOAPISession



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid_session** | **str** | Richiedi o modifica unique identifier session. | [optional] 
**utente** | [**DTOAPIUser**](DTOAPIUser.md) |  | [optional] 
**start_session** | **datetime** | Richiedi o modifica start session. | [optional] 
**expired** | **int** | Richiedi o modifica expired. | [optional] 

## Example

```python
from openapi_client.models.dtoapi_session import DTOAPISession

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPISession from a JSON string
dtoapi_session_instance = DTOAPISession.from_json(json)
# print the JSON string representation of the object
print DTOAPISession.to_json()

# convert the object into a dict
dtoapi_session_dict = dtoapi_session_instance.to_dict()
# create an instance of DTOAPISession from a dict
dtoapi_session_form_dict = dtoapi_session.from_dict(dtoapi_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


