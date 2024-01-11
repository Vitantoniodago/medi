# DTOAPIPrescrizioni



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prescrizione** | [**List[DTOPrescrizione]**](DTOPrescrizione.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_prescrizioni import DTOAPIPrescrizioni

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIPrescrizioni from a JSON string
dtoapi_prescrizioni_instance = DTOAPIPrescrizioni.from_json(json)
# print the JSON string representation of the object
print DTOAPIPrescrizioni.to_json()

# convert the object into a dict
dtoapi_prescrizioni_dict = dtoapi_prescrizioni_instance.to_dict()
# create an instance of DTOAPIPrescrizioni from a dict
dtoapi_prescrizioni_form_dict = dtoapi_prescrizioni.from_dict(dtoapi_prescrizioni_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


