# DTOAPIDiarioClinico



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diario_clinico** | [**List[DTODiarioClinico]**](DTODiarioClinico.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_diario_clinico import DTOAPIDiarioClinico

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIDiarioClinico from a JSON string
dtoapi_diario_clinico_instance = DTOAPIDiarioClinico.from_json(json)
# print the JSON string representation of the object
print DTOAPIDiarioClinico.to_json()

# convert the object into a dict
dtoapi_diario_clinico_dict = dtoapi_diario_clinico_instance.to_dict()
# create an instance of DTOAPIDiarioClinico from a dict
dtoapi_diario_clinico_form_dict = dtoapi_diario_clinico.from_dict(dtoapi_diario_clinico_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


