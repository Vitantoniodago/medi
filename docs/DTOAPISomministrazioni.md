# DTOAPISomministrazioni



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**somministrazione** | [**List[DTOSomministrazione]**](DTOSomministrazione.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_somministrazioni import DTOAPISomministrazioni

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPISomministrazioni from a JSON string
dtoapi_somministrazioni_instance = DTOAPISomministrazioni.from_json(json)
# print the JSON string representation of the object
print DTOAPISomministrazioni.to_json()

# convert the object into a dict
dtoapi_somministrazioni_dict = dtoapi_somministrazioni_instance.to_dict()
# create an instance of DTOAPISomministrazioni from a dict
dtoapi_somministrazioni_form_dict = dtoapi_somministrazioni.from_dict(dtoapi_somministrazioni_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


