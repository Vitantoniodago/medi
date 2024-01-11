# DTOAPIDocumento


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice_documento** | **str** |  | [optional] 
**sessione** | [**DTOAPISession**](DTOAPISession.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_documento import DTOAPIDocumento

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIDocumento from a JSON string
dtoapi_documento_instance = DTOAPIDocumento.from_json(json)
# print the JSON string representation of the object
print DTOAPIDocumento.to_json()

# convert the object into a dict
dtoapi_documento_dict = dtoapi_documento_instance.to_dict()
# create an instance of DTOAPIDocumento from a dict
dtoapi_documento_form_dict = dtoapi_documento.from_dict(dtoapi_documento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


