# DTOAPIVisitaPaziente


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**codice_fiscale** | **str** |  | [optional] 
**nome** | **str** |  | [optional] 
**cognome** | **str** |  | [optional] 
**data_nascita** | **datetime** |  | [optional] 
**comune_nascita** | **str** |  | [optional] 
**stato_coscienza** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_visita_paziente import DTOAPIVisitaPaziente

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIVisitaPaziente from a JSON string
dtoapi_visita_paziente_instance = DTOAPIVisitaPaziente.from_json(json)
# print the JSON string representation of the object
print DTOAPIVisitaPaziente.to_json()

# convert the object into a dict
dtoapi_visita_paziente_dict = dtoapi_visita_paziente_instance.to_dict()
# create an instance of DTOAPIVisitaPaziente from a dict
dtoapi_visita_paziente_form_dict = dtoapi_visita_paziente.from_dict(dtoapi_visita_paziente_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


