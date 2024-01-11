# DTOPrescrizione



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_farmaco** | **int** | Richiedi o modifica identifier farmaco. | [optional] 
**farmaco** | **str** |  | [optional] 
**id_unita** | **int** | Richiedi o modifica identifier unita. | [optional] 
**id_modalita_somministrazione** | **int** | Richiedi o modifica identifier modalita somministrazione. | [optional] 
**id_via_somministrazione** | **int** | Richiedi o modifica identifier via somministrazione. | [optional] 
**inizio_terapia** | **datetime** | Richiedi o modifica inizio terapia. | [optional] 
**fine_terapia** | **datetime** | Richiedi o modifica fine terapia. | [optional] 
**durata_terapia** | **int** | Richiedi o modifica durata terapia. | [optional] 
**note** | **str** | Richiedi o modifica note. | [optional] 
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**id_prescrizione** | **int** | Richiedi o modifica identifier prescrizione. | [optional] 
**id_modalita_ora_somministrazione** | **int** | Richiedi o modifica identifier modalita ora somministrazione. | [optional] 
**modelli** | [**List[DTOItemPrescrizione]**](DTOItemPrescrizione.md) | Richiedi o modifica modelli. | [optional] 
**somministrazione_colazione** | **bool** | Richiedi o modifica somministrazione colazione. | [optional] 
**somministrato** | **bool** |  | [optional] 
**ora_colazione** | **datetime** | Richiedi o modifica ora colazione. | [optional] 
**somministrazione_pranzo** | **bool** | Richiedi o modifica somministrazione pranzo. | [optional] 
**ora_pranzo** | **datetime** | Richiedi o modifica ora pranzo. | [optional] 
**somministrazione_cena** | **bool** | Richiedi o modifica somministrazione cena. | [optional] 
**ora_cena** | **datetime** | Richiedi o modifica ora cena. | [optional] 
**ora_inizio** | **datetime** | Richiedi o modifica ora inizio. | [optional] 
**ora_fine** | **datetime** | Richiedi o modifica ora fine. | [optional] 
**id_visita** | **int** |  | [optional] 
**assistito** | [**DTOAPIAssistito**](DTOAPIAssistito.md) |  | [optional] 

## Example

```python
from openapi_client.models.dto_prescrizione import DTOPrescrizione

# TODO update the JSON string below
json = "{}"
# create an instance of DTOPrescrizione from a JSON string
dto_prescrizione_instance = DTOPrescrizione.from_json(json)
# print the JSON string representation of the object
print DTOPrescrizione.to_json()

# convert the object into a dict
dto_prescrizione_dict = dto_prescrizione_instance.to_dict()
# create an instance of DTOPrescrizione from a dict
dto_prescrizione_form_dict = dto_prescrizione.from_dict(dto_prescrizione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


