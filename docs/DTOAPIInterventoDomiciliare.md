# DTOAPIInterventoDomiciliare



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice_prestazione** | **str** | Richiedi o modifica codice prestazione. | [optional] 
**id_ordine_lavoro** | **int** | Richiedi o modifica identifier ordine lavoro. | [optional] 
**data_inizio** | **datetime** | Richiedi o modifica data inizio. | [optional] 
**data_fine** | **datetime** | Richiedi o modifica data fine. | [optional] 
**medi_box** | **str** | Richiedi o modifica medi box. | [optional] 
**room** | **str** | Richiedi o modifica room. | [optional] 
**id_operatore** | **int** | Richiedi o modifica identifier operatore. | [optional] 
**attivato** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOAPIInterventoDomiciliare} is attivato. | [optional] 
**attivita_intervento** | [**DTOAPIAttivitaEsterna**](DTOAPIAttivitaEsterna.md) |  | [optional] 
**guid_assistito** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_intervento_domiciliare import DTOAPIInterventoDomiciliare

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIInterventoDomiciliare from a JSON string
dtoapi_intervento_domiciliare_instance = DTOAPIInterventoDomiciliare.from_json(json)
# print the JSON string representation of the object
print DTOAPIInterventoDomiciliare.to_json()

# convert the object into a dict
dtoapi_intervento_domiciliare_dict = dtoapi_intervento_domiciliare_instance.to_dict()
# create an instance of DTOAPIInterventoDomiciliare from a dict
dtoapi_intervento_domiciliare_form_dict = dtoapi_intervento_domiciliare.from_dict(dtoapi_intervento_domiciliare_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


