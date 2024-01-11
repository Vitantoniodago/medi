# DTOAPIAttivitaEsterna



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_ordine_lavoro** | **int** | Richiedi o modifica identifier ordine lavoro. | [optional] 
**codice** | **str** | Richiedi o modifica codice. | [optional] 
**id_turno** | **int** | Richiedi o modifica identifier turno. | [optional] 
**id_sostituzione_turno** | **int** | Richiedi o modifica identifier sostituzione turno. | [optional] 
**data_inizio** | **datetime** | Richiedi o modifica data inizio. | [optional] 
**data_fine** | **datetime** | Richiedi o modifica data fine. | [optional] 
**assistito** | [**DTOAPIAssistito**](DTOAPIAssistito.md) |  | [optional] 
**prestazioni** | [**List[DTOAPIPrestazione]**](DTOAPIPrestazione.md) | Richiedi o modifica prestazioni. | [optional] 
**operatore** | [**DTOAPIOperatore**](DTOAPIOperatore.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_attivita_esterna import DTOAPIAttivitaEsterna

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIAttivitaEsterna from a JSON string
dtoapi_attivita_esterna_instance = DTOAPIAttivitaEsterna.from_json(json)
# print the JSON string representation of the object
print DTOAPIAttivitaEsterna.to_json()

# convert the object into a dict
dtoapi_attivita_esterna_dict = dtoapi_attivita_esterna_instance.to_dict()
# create an instance of DTOAPIAttivitaEsterna from a dict
dtoapi_attivita_esterna_form_dict = dtoapi_attivita_esterna.from_dict(dtoapi_attivita_esterna_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


