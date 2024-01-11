# DTOAPIEsamiObiettivo



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esame_obiettivo_generale** | [**List[DTOEsameObiettivoGenerale]**](DTOEsameObiettivoGenerale.md) |  | [optional] 
**esame_obiettivo_regionale** | [**List[DTOEsameObiettivoRegionale]**](DTOEsameObiettivoRegionale.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_esami_obiettivo import DTOAPIEsamiObiettivo

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIEsamiObiettivo from a JSON string
dtoapi_esami_obiettivo_instance = DTOAPIEsamiObiettivo.from_json(json)
# print the JSON string representation of the object
print DTOAPIEsamiObiettivo.to_json()

# convert the object into a dict
dtoapi_esami_obiettivo_dict = dtoapi_esami_obiettivo_instance.to_dict()
# create an instance of DTOAPIEsamiObiettivo from a dict
dtoapi_esami_obiettivo_form_dict = dtoapi_esami_obiettivo.from_dict(dtoapi_esami_obiettivo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


