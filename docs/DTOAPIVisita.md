# DTOAPIVisita


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identificativo** | **str** |  | [optional] 
**data_intervento** | **datetime** |  | [optional] 
**data_invio** | **datetime** |  | [optional] 
**refertato** | **bool** |  | [optional] 
**paziente** | [**DTOAPIVisitaPaziente**](DTOAPIVisitaPaziente.md) |  | [optional] 
**esami_ecg** | [**List[DTOAPIVisitaECG]**](DTOAPIVisitaECG.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_visita import DTOAPIVisita

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIVisita from a JSON string
dtoapi_visita_instance = DTOAPIVisita.from_json(json)
# print the JSON string representation of the object
print DTOAPIVisita.to_json()

# convert the object into a dict
dtoapi_visita_dict = dtoapi_visita_instance.to_dict()
# create an instance of DTOAPIVisita from a dict
dtoapi_visita_form_dict = dtoapi_visita.from_dict(dtoapi_visita_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


