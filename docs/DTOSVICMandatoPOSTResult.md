# DTOSVICMandatoPOSTResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anno** | **int** |  | [optional] 
**numero** | **int** |  | [optional] 
**codice_errore** | **str** |  | [optional] 
**errore** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dtosvic_mandato_post_result import DTOSVICMandatoPOSTResult

# TODO update the JSON string below
json = "{}"
# create an instance of DTOSVICMandatoPOSTResult from a JSON string
dtosvic_mandato_post_result_instance = DTOSVICMandatoPOSTResult.from_json(json)
# print the JSON string representation of the object
print DTOSVICMandatoPOSTResult.to_json()

# convert the object into a dict
dtosvic_mandato_post_result_dict = dtosvic_mandato_post_result_instance.to_dict()
# create an instance of DTOSVICMandatoPOSTResult from a dict
dtosvic_mandato_post_result_form_dict = dtosvic_mandato_post_result.from_dict(dtosvic_mandato_post_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


