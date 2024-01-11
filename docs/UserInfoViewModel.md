# UserInfoViewModel



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Richiedi o modifica email. | [optional] 
**has_registered** | **bool** | Richiedi o modifica un valore che indica this instance has registered. | [optional] 
**login_provider** | **str** | Richiedi o modifica login provider. | [optional] 

## Example

```python
from openapi_client.models.user_info_view_model import UserInfoViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of UserInfoViewModel from a JSON string
user_info_view_model_instance = UserInfoViewModel.from_json(json)
# print the JSON string representation of the object
print UserInfoViewModel.to_json()

# convert the object into a dict
user_info_view_model_dict = user_info_view_model_instance.to_dict()
# create an instance of UserInfoViewModel from a dict
user_info_view_model_form_dict = user_info_view_model.from_dict(user_info_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


