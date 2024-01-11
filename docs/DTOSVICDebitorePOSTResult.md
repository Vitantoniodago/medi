# DTOSVICDebitorePOSTResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice_debitore** | **str** |  | [optional] 
**codice_errore** | **str** |  | [optional] 
**errore** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dtosvic_debitore_post_result import DTOSVICDebitorePOSTResult

# TODO update the JSON string below
json = "{}"
# create an instance of DTOSVICDebitorePOSTResult from a JSON string
dtosvic_debitore_post_result_instance = DTOSVICDebitorePOSTResult.from_json(json)
# print the JSON string representation of the object
print DTOSVICDebitorePOSTResult.to_json()

# convert the object into a dict
dtosvic_debitore_post_result_dict = dtosvic_debitore_post_result_instance.to_dict()
# create an instance of DTOSVICDebitorePOSTResult from a dict
dtosvic_debitore_post_result_form_dict = dtosvic_debitore_post_result.from_dict(dtosvic_debitore_post_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


