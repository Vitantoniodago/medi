# DTOSVICDebitorePOST


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice_debitore** | **str** |  | [optional] 
**tipo_anagrafica** | **str** |  | [optional] 
**ragione_sociale** | **str** |  | [optional] 
**cognome** | **str** |  | [optional] 
**nome** | **str** |  | [optional] 
**sesso** | **str** |  | [optional] 
**data_nascita** | **datetime** |  | [optional] 
**localit_nascita** | **str** |  | [optional] 
**provincia_nascita** | **str** |  | [optional] 
**partita_iva** | **str** |  | [optional] 
**codice_fiscale** | **str** |  | [optional] 
**indirizzo** | **str** |  | [optional] 
**localit** | **str** |  | [optional] 
**cap** | **str** |  | [optional] 
**provincia** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**telefono** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dtosvic_debitore_post import DTOSVICDebitorePOST

# TODO update the JSON string below
json = "{}"
# create an instance of DTOSVICDebitorePOST from a JSON string
dtosvic_debitore_post_instance = DTOSVICDebitorePOST.from_json(json)
# print the JSON string representation of the object
print DTOSVICDebitorePOST.to_json()

# convert the object into a dict
dtosvic_debitore_post_dict = dtosvic_debitore_post_instance.to_dict()
# create an instance of DTOSVICDebitorePOST from a dict
dtosvic_debitore_post_form_dict = dtosvic_debitore_post.from_dict(dtosvic_debitore_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


