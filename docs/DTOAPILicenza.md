# DTOAPILicenza


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_attivazione** | **datetime** |  | [optional] 
**tipologia_licenza** | **str** |  | [optional] 
**url_riferimento** | **str** |  | [optional] 
**api_key_licensed** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_licenza import DTOAPILicenza

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPILicenza from a JSON string
dtoapi_licenza_instance = DTOAPILicenza.from_json(json)
# print the JSON string representation of the object
print DTOAPILicenza.to_json()

# convert the object into a dict
dtoapi_licenza_dict = dtoapi_licenza_instance.to_dict()
# create an instance of DTOAPILicenza from a dict
dtoapi_licenza_form_dict = dtoapi_licenza.from_dict(dtoapi_licenza_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


