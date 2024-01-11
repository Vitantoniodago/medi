# DTOAPIAzienda


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ragione_sociale** | **str** |  | [optional] 
**codice_azienda** | **str** |  | [optional] 
**partita_iva** | **str** |  | [optional] 
**codice_fiscale** | **str** |  | [optional] 
**indirizzo** | **str** |  | [optional] 
**pec** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**comune** | **str** |  | [optional] 
**provincia** | **str** |  | [optional] 
**cap** | **str** |  | [optional] 
**sede_riferimento** | **str** |  | [optional] 
**categoria** | [**DTOAPICategoria**](DTOAPICategoria.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_azienda import DTOAPIAzienda

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIAzienda from a JSON string
dtoapi_azienda_instance = DTOAPIAzienda.from_json(json)
# print the JSON string representation of the object
print DTOAPIAzienda.to_json()

# convert the object into a dict
dtoapi_azienda_dict = dtoapi_azienda_instance.to_dict()
# create an instance of DTOAPIAzienda from a dict
dtoapi_azienda_form_dict = dtoapi_azienda.from_dict(dtoapi_azienda_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


