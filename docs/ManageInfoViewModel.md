# ManageInfoViewModel



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_login_provider** | **str** | Richiedi o modifica local login provider. | [optional] 
**email** | **str** | Richiedi o modifica email. | [optional] 
**logins** | [**List[UserLoginInfoViewModel]**](UserLoginInfoViewModel.md) | Richiedi o modifica logins. | [optional] 
**external_login_providers** | [**List[ExternalLoginViewModel]**](ExternalLoginViewModel.md) | Richiedi o modifica external login providers. | [optional] 

## Example

```python
from openapi_client.models.manage_info_view_model import ManageInfoViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of ManageInfoViewModel from a JSON string
manage_info_view_model_instance = ManageInfoViewModel.from_json(json)
# print the JSON string representation of the object
print ManageInfoViewModel.to_json()

# convert the object into a dict
manage_info_view_model_dict = manage_info_view_model_instance.to_dict()
# create an instance of ManageInfoViewModel from a dict
manage_info_view_model_form_dict = manage_info_view_model.from_dict(manage_info_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


