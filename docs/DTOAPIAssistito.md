# DTOAPIAssistito



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid_assistito** | **str** | Richiedi o modifica unique identifier assistito. | [optional] 
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**nome** | **str** | Richiedi o modifica nome. | [optional] 
**cognome** | **str** | Richiedi o modifica cognome. | [optional] 
**codice_fiscale** | **str** |  | [optional] 
**data_nascita** | **datetime** |  | [optional] 
**sesso** | **int** |  | [optional] 
**comune** | **str** | Richiedi o modifica comune. | [optional] 
**indirizzo** | **str** | Richiedi o modifica indirizzo. | [optional] 
**cap** | **str** | Richiedi o modifica cap. | [optional] 
**anamnesi** | [**DTOAPIAnamnesi**](DTOAPIAnamnesi.md) |  | [optional] 
**esami_obiettivo** | [**DTOAPIEsamiObiettivo**](DTOAPIEsamiObiettivo.md) |  | [optional] 
**esami_strumentali** | [**DTOAPIEsamiStrumentale**](DTOAPIEsamiStrumentale.md) |  | [optional] 
**prescrizioni** | [**DTOAPIPrescrizioni**](DTOAPIPrescrizioni.md) |  | [optional] 
**somministrazioni** | [**DTOAPISomministrazioni**](DTOAPISomministrazioni.md) |  | [optional] 
**prestazioni_fisioterapiche** | [**DTOAPIPrestazioniFisioterapiche**](DTOAPIPrestazioniFisioterapiche.md) |  | [optional] 
**diari_clinici** | [**DTOAPIDiarioClinico**](DTOAPIDiarioClinico.md) |  | [optional] 
**bisogni_paziente** | [**DTOAPIBisogniPaziente**](DTOAPIBisogniPaziente.md) |  | [optional] 
**elenco_note** | [**DTOAPINote**](DTOAPINote.md) |  | [optional] 
**consensi** | [**DTOAPIConsensi**](DTOAPIConsensi.md) |  | [optional] 
**sessione** | [**DTOAPISession**](DTOAPISession.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_assistito import DTOAPIAssistito

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIAssistito from a JSON string
dtoapi_assistito_instance = DTOAPIAssistito.from_json(json)
# print the JSON string representation of the object
print DTOAPIAssistito.to_json()

# convert the object into a dict
dtoapi_assistito_dict = dtoapi_assistito_instance.to_dict()
# create an instance of DTOAPIAssistito from a dict
dtoapi_assistito_form_dict = dtoapi_assistito.from_dict(dtoapi_assistito_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


