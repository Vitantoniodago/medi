# ExternalLoginViewModel



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Richiedi o modifica name. | [optional] 
**url** | **str** | Richiedi o modifica URL. | [optional] 
**state** | **str** | Richiedi o modifica state. | [optional] 

## Example

```python
from openapi_client.models.external_login_view_model import ExternalLoginViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalLoginViewModel from a JSON string
external_login_view_model_instance = ExternalLoginViewModel.from_json(json)
# print the JSON string representation of the object
print ExternalLoginViewModel.to_json()

# convert the object into a dict
external_login_view_model_dict = external_login_view_model_instance.to_dict()
# create an instance of ExternalLoginViewModel from a dict
external_login_view_model_form_dict = external_login_view_model.from_dict(external_login_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


