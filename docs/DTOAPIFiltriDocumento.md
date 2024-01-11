# DTOAPIFiltriDocumento


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice_documento** | **str** |  | [optional] 
**data_inizio** | **datetime** |  | [optional] 
**data_fine** | **datetime** |  | [optional] 
**codice_fiscale** | **str** |  | [optional] 
**partita_iva** | **str** |  | [optional] 
**ragione_sociale** | **str** |  | [optional] 
**sessione** | [**DTOAPISession**](DTOAPISession.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_filtri_documento import DTOAPIFiltriDocumento

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIFiltriDocumento from a JSON string
dtoapi_filtri_documento_instance = DTOAPIFiltriDocumento.from_json(json)
# print the JSON string representation of the object
print DTOAPIFiltriDocumento.to_json()

# convert the object into a dict
dtoapi_filtri_documento_dict = dtoapi_filtri_documento_instance.to_dict()
# create an instance of DTOAPIFiltriDocumento from a dict
dtoapi_filtri_documento_form_dict = dtoapi_filtri_documento.from_dict(dtoapi_filtri_documento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


