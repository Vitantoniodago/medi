# DTOBisogniPazienteMobilizzazione



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ausilio_letto** | **bool** | Richiedi o modifica un valore che indica [ausilio letto]. | [optional] 
**aiuto_seduta** | **bool** | Richiedi o modifica un valore che indica [aiuto seduta]. | [optional] 
**movimenti_volontari** | **bool** | Richiedi o modifica un valore che indica [movimenti volontari]. | [optional] 
**rotazione_corpo** | **bool** | Richiedi o modifica un valore che indica [rotazione corpo]. | [optional] 
**aiuto_deambulazione** | **bool** | Richiedi o modifica un valore che indica [aiuto deambulazione]. | [optional] 
**permanenza_letto_forzata** | **bool** | Richiedi o modifica un valore che indica [permanenza letto forzata]. | [optional] 
**disabile_allettato** | **bool** | Richiedi o modifica un valore che indica [disabile allettato]. | [optional] 
**mobilizzazione_strumenti** | **bool** | Richiedi o modifica un valore che indica [mobilizzazione strumenti]. | [optional] 
**lesioni_ossee** | **bool** | Richiedi o modifica un valore che indica [lesioni ossee]. | [optional] 
**lombagia_acuta** | **bool** | Richiedi o modifica un valore che indica [lombagia acuta]. | [optional] 
**cervicoalgia_acuta** | **bool** | Richiedi o modifica un valore che indica [cervicoalgia acuta]. | [optional] 
**paraplegia** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteMobilizzazione} is paraplegia. | [optional] 
**emiplegia** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteMobilizzazione} is emiplegia. | [optional] 
**tetraplegia** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteMobilizzazione} is tetraplegia. | [optional] 
**id_amputazione** | **int** | Richiedi o modifica identifier amputazione. | [optional] 
**note_amputazione** | **str** | Richiedi o modifica note amputazione. | [optional] 
**note** | **str** | Richiedi o modifica note. | [optional] 
**id_analisi_bisogni_mobilizzazione** | **int** | Richiedi o modifica identifier analisi bisogni mobilizzazione. | [optional] 
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**id_visita** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dto_bisogni_paziente_mobilizzazione import DTOBisogniPazienteMobilizzazione

# TODO update the JSON string below
json = "{}"
# create an instance of DTOBisogniPazienteMobilizzazione from a JSON string
dto_bisogni_paziente_mobilizzazione_instance = DTOBisogniPazienteMobilizzazione.from_json(json)
# print the JSON string representation of the object
print DTOBisogniPazienteMobilizzazione.to_json()

# convert the object into a dict
dto_bisogni_paziente_mobilizzazione_dict = dto_bisogni_paziente_mobilizzazione_instance.to_dict()
# create an instance of DTOBisogniPazienteMobilizzazione from a dict
dto_bisogni_paziente_mobilizzazione_form_dict = dto_bisogni_paziente_mobilizzazione.from_dict(dto_bisogni_paziente_mobilizzazione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


