# DTOSVICRigaMandato


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice_creditore** | **str** |  | [optional] 
**importo** | **str** |  | [optional] 
**nota** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dtosvic_riga_mandato import DTOSVICRigaMandato

# TODO update the JSON string below
json = "{}"
# create an instance of DTOSVICRigaMandato from a JSON string
dtosvic_riga_mandato_instance = DTOSVICRigaMandato.from_json(json)
# print the JSON string representation of the object
print DTOSVICRigaMandato.to_json()

# convert the object into a dict
dtosvic_riga_mandato_dict = dtosvic_riga_mandato_instance.to_dict()
# create an instance of DTOSVICRigaMandato from a dict
dtosvic_riga_mandato_form_dict = dtosvic_riga_mandato.from_dict(dtosvic_riga_mandato_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


