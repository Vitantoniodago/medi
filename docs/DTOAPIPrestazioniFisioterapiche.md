# DTOAPIPrestazioniFisioterapiche



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prestazione_fisioterapica** | [**List[DTOPrestazione]**](DTOPrestazione.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_prestazioni_fisioterapiche import DTOAPIPrestazioniFisioterapiche

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIPrestazioniFisioterapiche from a JSON string
dtoapi_prestazioni_fisioterapiche_instance = DTOAPIPrestazioniFisioterapiche.from_json(json)
# print the JSON string representation of the object
print DTOAPIPrestazioniFisioterapiche.to_json()

# convert the object into a dict
dtoapi_prestazioni_fisioterapiche_dict = dtoapi_prestazioni_fisioterapiche_instance.to_dict()
# create an instance of DTOAPIPrestazioniFisioterapiche from a dict
dtoapi_prestazioni_fisioterapiche_form_dict = dtoapi_prestazioni_fisioterapiche.from_dict(dtoapi_prestazioni_fisioterapiche_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


