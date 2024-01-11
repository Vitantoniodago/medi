# DTOAPICategoria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**categoria** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_categoria import DTOAPICategoria

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPICategoria from a JSON string
dtoapi_categoria_instance = DTOAPICategoria.from_json(json)
# print the JSON string representation of the object
print DTOAPICategoria.to_json()

# convert the object into a dict
dtoapi_categoria_dict = dtoapi_categoria_instance.to_dict()
# create an instance of DTOAPICategoria from a dict
dtoapi_categoria_form_dict = dtoapi_categoria.from_dict(dtoapi_categoria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


