# DTOAPIUser



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Richiedi o modifica unique identifier. | [optional] 
**user_name** | **str** | Richiedi o modifica name of the user. | [optional] 
**email** | **str** | Richiedi o modifica email. | [optional] 
**password** | **str** | Richiedi o modifica password. | [optional] 
**tipologia** | **str** | Richiedi o modifica tipologia. | [optional] 
**api_key** | **str** | Richiedi o modifica API key. | [optional] 
**nome** | **str** | Richiedi o modifica nome. | [optional] 
**cognome** | **str** | Richiedi o modifica cognome. | [optional] 
**ruolo** | **str** | Richiedi o modifica ruolo. | [optional] 
**id_tipologia** | **int** | Richiedi o modifica identifier tipologia. | [optional] 
**codice_fiscale** | **str** | Richiedi o modifica codice fiscale. | [optional] 
**guid_medibox** | **str** | Richiedi o modifica unique identifier medibox. | [optional] 

## Example

```python
from openapi_client.models.dtoapi_user import DTOAPIUser

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIUser from a JSON string
dtoapi_user_instance = DTOAPIUser.from_json(json)
# print the JSON string representation of the object
print DTOAPIUser.to_json()

# convert the object into a dict
dtoapi_user_dict = dtoapi_user_instance.to_dict()
# create an instance of DTOAPIUser from a dict
dtoapi_user_form_dict = dtoapi_user.from_dict(dtoapi_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


