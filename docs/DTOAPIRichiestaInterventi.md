# DTOAPIRichiestaInterventi



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_operatore** | **int** | Richiedi o modifica identifier operatore. | [optional] 
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**guid_medibox** | **str** | Richiedi o modifica unique identifier medibox. | [optional] 
**data_riferimento** | **datetime** | Richiedi o modifica data riferimento. | [optional] 

## Example

```python
from openapi_client.models.dtoapi_richiesta_interventi import DTOAPIRichiestaInterventi

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIRichiestaInterventi from a JSON string
dtoapi_richiesta_interventi_instance = DTOAPIRichiestaInterventi.from_json(json)
# print the JSON string representation of the object
print DTOAPIRichiestaInterventi.to_json()

# convert the object into a dict
dtoapi_richiesta_interventi_dict = dtoapi_richiesta_interventi_instance.to_dict()
# create an instance of DTOAPIRichiestaInterventi from a dict
dtoapi_richiesta_interventi_form_dict = dtoapi_richiesta_interventi.from_dict(dtoapi_richiesta_interventi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


