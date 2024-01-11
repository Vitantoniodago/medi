# DTOBisogniPazienteIgiene



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aiuto_igiene** | **bool** | Richiedi o modifica un valore che indica [aiuto igiene]. | [optional] 
**strumenti_igiene** | **bool** | Richiedi o modifica un valore che indica [strumenti igiene]. | [optional] 
**aiuto_bagno** | **bool** | Richiedi o modifica un valore che indica [aiuto bagno]. | [optional] 
**bagno_letto** | **bool** | Richiedi o modifica un valore che indica [bagno letto]. | [optional] 
**aiuto_vestizione** | **bool** | Richiedi o modifica un valore che indica [aiuto vestizione]. | [optional] 
**piaghe_decubito** | **bool** | Richiedi o modifica un valore che indica [piaghe decubito]. | [optional] 
**aiuto_doccia** | **bool** | Richiedi o modifica un valore che indica [aiuto doccia]. | [optional] 
**aiuto_shampoo** | **bool** | Richiedi o modifica un valore che indica [aiuto shampoo]. | [optional] 
**aiuto_pediluvio** | **bool** | Richiedi o modifica un valore che indica [aiuto pediluvio]. | [optional] 
**aiuto_estetico** | **bool** | Richiedi o modifica un valore che indica [aiuto estetico]. | [optional] 
**igiene_catetere** | **bool** | Richiedi o modifica un valore che indica [igiene catetere]. | [optional] 
**igiene_stormie** | **bool** | Richiedi o modifica un valore che indica [igiene stormie]. | [optional] 
**igiene_incontinenza** | **bool** | Richiedi o modifica un valore che indica [igiene incontinenza]. | [optional] 
**ustioni** | **str** | Richiedi o modifica ustioni. | [optional] 
**ferite** | **str** | Richiedi o modifica ferite. | [optional] 
**malattie_pelle** | **str** | Richiedi o modifica malattie pelle. | [optional] 
**note** | **str** | Richiedi o modifica note. | [optional] 
**id_analisi_bisogni_igiene** | **int** | Richiedi o modifica identifier analisi bisogni igiene. | [optional] 
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**id_visita** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dto_bisogni_paziente_igiene import DTOBisogniPazienteIgiene

# TODO update the JSON string below
json = "{}"
# create an instance of DTOBisogniPazienteIgiene from a JSON string
dto_bisogni_paziente_igiene_instance = DTOBisogniPazienteIgiene.from_json(json)
# print the JSON string representation of the object
print DTOBisogniPazienteIgiene.to_json()

# convert the object into a dict
dto_bisogni_paziente_igiene_dict = dto_bisogni_paziente_igiene_instance.to_dict()
# create an instance of DTOBisogniPazienteIgiene from a dict
dto_bisogni_paziente_igiene_form_dict = dto_bisogni_paziente_igiene.from_dict(dto_bisogni_paziente_igiene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


