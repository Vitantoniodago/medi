# UserLoginInfoViewModel



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_provider** | **str** | Richiedi o modifica login provider. | [optional] 
**provider_key** | **str** | Richiedi o modifica provider key. | [optional] 

## Example

```python
from openapi_client.models.user_login_info_view_model import UserLoginInfoViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of UserLoginInfoViewModel from a JSON string
user_login_info_view_model_instance = UserLoginInfoViewModel.from_json(json)
# print the JSON string representation of the object
print UserLoginInfoViewModel.to_json()

# convert the object into a dict
user_login_info_view_model_dict = user_login_info_view_model_instance.to_dict()
# create an instance of UserLoginInfoViewModel from a dict
user_login_info_view_model_form_dict = user_login_info_view_model.from_dict(user_login_info_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


