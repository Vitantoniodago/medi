# DTOSVICRigaReversale


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice_debitore** | **str** |  | [optional] 
**importo** | **str** |  | [optional] 
**nota** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dtosvic_riga_reversale import DTOSVICRigaReversale

# TODO update the JSON string below
json = "{}"
# create an instance of DTOSVICRigaReversale from a JSON string
dtosvic_riga_reversale_instance = DTOSVICRigaReversale.from_json(json)
# print the JSON string representation of the object
print DTOSVICRigaReversale.to_json()

# convert the object into a dict
dtosvic_riga_reversale_dict = dtosvic_riga_reversale_instance.to_dict()
# create an instance of DTOSVICRigaReversale from a dict
dtosvic_riga_reversale_form_dict = dtosvic_riga_reversale.from_dict(dtosvic_riga_reversale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


