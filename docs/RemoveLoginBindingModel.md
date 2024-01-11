# RemoveLoginBindingModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_provider** | **str** |  | 
**provider_key** | **str** |  | 

## Example

```python
from openapi_client.models.remove_login_binding_model import RemoveLoginBindingModel

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveLoginBindingModel from a JSON string
remove_login_binding_model_instance = RemoveLoginBindingModel.from_json(json)
# print the JSON string representation of the object
print RemoveLoginBindingModel.to_json()

# convert the object into a dict
remove_login_binding_model_dict = remove_login_binding_model_instance.to_dict()
# create an instance of RemoveLoginBindingModel from a dict
remove_login_binding_model_form_dict = remove_login_binding_model.from_dict(remove_login_binding_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


