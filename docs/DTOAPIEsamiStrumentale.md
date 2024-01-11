# DTOAPIEsamiStrumentale



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esame_strumentale_conclusione** | [**List[DTOEsameStrumentaleConclusioneTerapia]**](DTOEsameStrumentaleConclusioneTerapia.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_esami_strumentale import DTOAPIEsamiStrumentale

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIEsamiStrumentale from a JSON string
dtoapi_esami_strumentale_instance = DTOAPIEsamiStrumentale.from_json(json)
# print the JSON string representation of the object
print DTOAPIEsamiStrumentale.to_json()

# convert the object into a dict
dtoapi_esami_strumentale_dict = dtoapi_esami_strumentale_instance.to_dict()
# create an instance of DTOAPIEsamiStrumentale from a dict
dtoapi_esami_strumentale_form_dict = dtoapi_esami_strumentale.from_dict(dtoapi_esami_strumentale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


