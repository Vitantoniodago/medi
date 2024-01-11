# DTOAPIAnagrafica


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice_fiscale** | **str** |  | [optional] 
**nome** | **str** |  | [optional] 
**cognome** | **str** |  | [optional] 
**comune** | **str** |  | [optional] 
**provincia** | **str** |  | [optional] 
**indirizzo** | **str** |  | [optional] 
**cap** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_anagrafica import DTOAPIAnagrafica

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIAnagrafica from a JSON string
dtoapi_anagrafica_instance = DTOAPIAnagrafica.from_json(json)
# print the JSON string representation of the object
print DTOAPIAnagrafica.to_json()

# convert the object into a dict
dtoapi_anagrafica_dict = dtoapi_anagrafica_instance.to_dict()
# create an instance of DTOAPIAnagrafica from a dict
dtoapi_anagrafica_form_dict = dtoapi_anagrafica.from_dict(dtoapi_anagrafica_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


