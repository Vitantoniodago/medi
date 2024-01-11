# DTOAPIDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid_device** | **str** |  | [optional] 
**mac_address** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 
**messaggio** | **str** |  | [optional] 
**stato** | **int** |  | [optional] 
**licenza** | [**DTOAPILicenza**](DTOAPILicenza.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_device import DTOAPIDevice

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIDevice from a JSON string
dtoapi_device_instance = DTOAPIDevice.from_json(json)
# print the JSON string representation of the object
print DTOAPIDevice.to_json()

# convert the object into a dict
dtoapi_device_dict = dtoapi_device_instance.to_dict()
# create an instance of DTOAPIDevice from a dict
dtoapi_device_form_dict = dtoapi_device.from_dict(dtoapi_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


