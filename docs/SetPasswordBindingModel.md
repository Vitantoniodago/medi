# SetPasswordBindingModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_password** | **str** |  | 
**confirm_password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.set_password_binding_model import SetPasswordBindingModel

# TODO update the JSON string below
json = "{}"
# create an instance of SetPasswordBindingModel from a JSON string
set_password_binding_model_instance = SetPasswordBindingModel.from_json(json)
# print the JSON string representation of the object
print SetPasswordBindingModel.to_json()

# convert the object into a dict
set_password_binding_model_dict = set_password_binding_model_instance.to_dict()
# create an instance of SetPasswordBindingModel from a dict
set_password_binding_model_form_dict = set_password_binding_model.from_dict(set_password_binding_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


