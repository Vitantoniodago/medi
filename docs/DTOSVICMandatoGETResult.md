# DTOSVICMandatoGETResult


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
**anno_impegno** | **int** |  | [optional] 
**numero_impegno** | **int** |  | [optional] 
**competenza_residuo** | **str** |  | [optional] 
**dettaglio** | [**List[DTOSVICRigaMandato]**](DTOSVICRigaMandato.md) |  | [optional] 
**codice_errore** | **str** |  | [optional] 
**errore** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dtosvic_mandato_get_result import DTOSVICMandatoGETResult

# TODO update the JSON string below
json = "{}"
# create an instance of DTOSVICMandatoGETResult from a JSON string
dtosvic_mandato_get_result_instance = DTOSVICMandatoGETResult.from_json(json)
# print the JSON string representation of the object
print DTOSVICMandatoGETResult.to_json()

# convert the object into a dict
dtosvic_mandato_get_result_dict = dtosvic_mandato_get_result_instance.to_dict()
# create an instance of DTOSVICMandatoGETResult from a dict
dtosvic_mandato_get_result_form_dict = dtosvic_mandato_get_result.from_dict(dtosvic_mandato_get_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


