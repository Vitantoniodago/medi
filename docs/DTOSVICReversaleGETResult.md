# DTOSVICReversaleGETResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anno** | **int** |  | [optional] 
**numero** | **int** |  | [optional] 
**data_operazione** | **datetime** |  | [optional] 
**causale** | **str** |  | [optional] 
**capitolo** | **int** |  | [optional] 
**articolo** | **int** |  | [optional] 
**importo** | **float** |  | [optional] 
**anno_accertamento** | **int** |  | [optional] 
**numero_accertamento** | **int** |  | [optional] 
**competenza_residuo** | **str** |  | [optional] 
**dettaglio** | [**List[DTOSVICRigaReversale]**](DTOSVICRigaReversale.md) |  | [optional] 
**codice_errore** | **str** |  | [optional] 
**errore** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dtosvic_reversale_get_result import DTOSVICReversaleGETResult

# TODO update the JSON string below
json = "{}"
# create an instance of DTOSVICReversaleGETResult from a JSON string
dtosvic_reversale_get_result_instance = DTOSVICReversaleGETResult.from_json(json)
# print the JSON string representation of the object
print DTOSVICReversaleGETResult.to_json()

# convert the object into a dict
dtosvic_reversale_get_result_dict = dtosvic_reversale_get_result_instance.to_dict()
# create an instance of DTOSVICReversaleGETResult from a dict
dtosvic_reversale_get_result_form_dict = dtosvic_reversale_get_result.from_dict(dtosvic_reversale_get_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


