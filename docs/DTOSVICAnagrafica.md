# DTOSVICAnagrafica


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cognome** | **str** |  | [optional] 
**nome** | **str** |  | [optional] 
**sesso** | **str** |  | [optional] 
**data_nascita** | **datetime** |  | [optional] 
**codice_istat_comune_nascita** | **str** |  | [optional] 
**codice_fiscale** | **str** |  | [optional] 
**indirizzo_residenza** | **str** |  | [optional] 
**codice_istat_comune_residenza** | **str** |  | [optional] 
**cap_residenza** | **str** |  | [optional] 
**telefono** | **str** |  | [optional] 
**cellulare** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**pec** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dtosvic_anagrafica import DTOSVICAnagrafica

# TODO update the JSON string below
json = "{}"
# create an instance of DTOSVICAnagrafica from a JSON string
dtosvic_anagrafica_instance = DTOSVICAnagrafica.from_json(json)
# print the JSON string representation of the object
print DTOSVICAnagrafica.to_json()

# convert the object into a dict
dtosvic_anagrafica_dict = dtosvic_anagrafica_instance.to_dict()
# create an instance of DTOSVICAnagrafica from a dict
dtosvic_anagrafica_form_dict = dtosvic_anagrafica.from_dict(dtosvic_anagrafica_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


