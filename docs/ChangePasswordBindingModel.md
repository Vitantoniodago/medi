# ChangePasswordBindingModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_password** | **str** |  | 
**new_password** | **str** |  | 
**confirm_password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.change_password_binding_model import ChangePasswordBindingModel

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePasswordBindingModel from a JSON string
change_password_binding_model_instance = ChangePasswordBindingModel.from_json(json)
# print the JSON string representation of the object
print ChangePasswordBindingModel.to_json()

# convert the object into a dict
change_password_binding_model_dict = change_password_binding_model_instance.to_dict()
# create an instance of ChangePasswordBindingModel from a dict
change_password_binding_model_form_dict = change_password_binding_model.from_dict(change_password_binding_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


