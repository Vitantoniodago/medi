# DTOAPIVisitaECG


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tipo_file** | **int** |  | [optional] 
**path_file** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_visita_ecg import DTOAPIVisitaECG

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIVisitaECG from a JSON string
dtoapi_visita_ecg_instance = DTOAPIVisitaECG.from_json(json)
# print the JSON string representation of the object
print DTOAPIVisitaECG.to_json()

# convert the object into a dict
dtoapi_visita_ecg_dict = dtoapi_visita_ecg_instance.to_dict()
# create an instance of DTOAPIVisitaECG from a dict
dtoapi_visita_ecg_form_dict = dtoapi_visita_ecg.from_dict(dtoapi_visita_ecg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


