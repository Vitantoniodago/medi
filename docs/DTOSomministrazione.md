# DTOSomministrazione



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_somministrazione** | **int** | Richiedi o modifica identifier somministrazione. | [optional] 
**prescrizione** | [**DTOPrescrizione**](DTOPrescrizione.md) |  | [optional] 
**modelli_parziali** | [**List[DTOModelloParziale]**](DTOModelloParziale.md) | Richiedi o modifica modelli parziali. | [optional] 

## Example

```python
from openapi_client.models.dto_somministrazione import DTOSomministrazione

# TODO update the JSON string below
json = "{}"
# create an instance of DTOSomministrazione from a JSON string
dto_somministrazione_instance = DTOSomministrazione.from_json(json)
# print the JSON string representation of the object
print DTOSomministrazione.to_json()

# convert the object into a dict
dto_somministrazione_dict = dto_somministrazione_instance.to_dict()
# create an instance of DTOSomministrazione from a dict
dto_somministrazione_form_dict = dto_somministrazione.from_dict(dto_somministrazione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


