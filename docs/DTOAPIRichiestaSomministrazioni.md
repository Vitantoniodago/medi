# DTOAPIRichiestaSomministrazioni


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_operatore** | **int** |  | [optional] 
**id_assistito** | **int** |  | [optional] 
**guid_medibox** | **str** |  | [optional] 
**data_riferimento** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_richiesta_somministrazioni import DTOAPIRichiestaSomministrazioni

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIRichiestaSomministrazioni from a JSON string
dtoapi_richiesta_somministrazioni_instance = DTOAPIRichiestaSomministrazioni.from_json(json)
# print the JSON string representation of the object
print DTOAPIRichiestaSomministrazioni.to_json()

# convert the object into a dict
dtoapi_richiesta_somministrazioni_dict = dtoapi_richiesta_somministrazioni_instance.to_dict()
# create an instance of DTOAPIRichiestaSomministrazioni from a dict
dtoapi_richiesta_somministrazioni_form_dict = dtoapi_richiesta_somministrazioni.from_dict(dtoapi_richiesta_somministrazioni_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


