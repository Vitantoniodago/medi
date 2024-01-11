# DTOPrestazione



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_prestazione** | **int** | Richiedi o modifica identifier prestazione. | [optional] 
**id_prestazione_planning** | **int** | Richiedi o modifica identifier prestazione planning. | [optional] 
**id_equipe** | **int** | Richiedi o modifica identifier equipe. | [optional] 
**id_pai** | **int** | Richiedi o modifica identifier pai. | [optional] 
**id_frequenza** | **int** |  | [optional] 
**durata** | **float** | Richiedi o modifica durata. | [optional] 
**codice** | **str** | Richiedi o modifica codice. | [optional] 
**descrizione** | **str** | Richiedi o modifica descrizione. | [optional] 
**assistito** | **str** | Richiedi o modifica assistito. | [optional] 
**inizio_prestazione** | **datetime** | Richiedi o modifica inizio prestazione. | [optional] 
**fine_prestazione** | **datetime** | Richiedi o modifica fine prestazione. | [optional] 
**note_prestazione** | **str** | Richiedi o modifica note prestazione. | [optional] 
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**durata_prestazione** | **int** | Richiedi o modifica durata prestazione. | [optional] 
**id_modalita_ora_prestazione** | **int** | Richiedi o modifica identifier modalita ora prestazione. | [optional] 
**modelli** | [**List[DTOItemPrestazioni]**](DTOItemPrestazioni.md) | Richiedi o modifica modelli. | [optional] 
**effettuata** | **bool** |  | [optional] 
**modelli_parziali** | [**List[DTOModelloParziale]**](DTOModelloParziale.md) | Richiedi o modifica modelli parziali. | [optional] 
**note_tipologia_accessi** | **str** |  | [optional] 
**struttura_erogante** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dto_prestazione import DTOPrestazione

# TODO update the JSON string below
json = "{}"
# create an instance of DTOPrestazione from a JSON string
dto_prestazione_instance = DTOPrestazione.from_json(json)
# print the JSON string representation of the object
print DTOPrestazione.to_json()

# convert the object into a dict
dto_prestazione_dict = dto_prestazione_instance.to_dict()
# create an instance of DTOPrestazione from a dict
dto_prestazione_form_dict = dto_prestazione.from_dict(dto_prestazione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


