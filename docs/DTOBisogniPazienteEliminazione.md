# DTOBisogniPazienteEliminazione



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ano_preternaturale** | **bool** | Richiedi o modifica un valore che indica [ano preternaturale]. | [optional] 
**proctorragia** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteEliminazione} is proctorragia. | [optional] 
**caterismo_intermittente** | **bool** | Richiedi o modifica un valore che indica [caterismo intermittente]. | [optional] 
**ritenzione_urinaria** | **bool** | Richiedi o modifica un valore che indica [ritenzione urinaria]. | [optional] 
**catetere_vescicale** | **bool** | Richiedi o modifica un valore che indica [catetere vescicale]. | [optional] 
**stipsi** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteEliminazione} is stipsi. | [optional] 
**dolori_addominali** | **bool** | Richiedi o modifica un valore che indica [dolori addominali]. | [optional] 
**tenesmo_rettale** | **bool** | Richiedi o modifica un valore che indica [tenesmo rettale]. | [optional] 
**drenaggio_transcutaneo** | **bool** | Richiedi o modifica un valore che indica [drenaggio transcutaneo]. | [optional] 
**tenesmo_vescicale** | **bool** | Richiedi o modifica un valore che indica [tenesmo vescicale]. | [optional] 
**ematuria** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteEliminazione} is ematuria. | [optional] 
**ureterostomie** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteEliminazione} is ureterostomie. | [optional] 
**id_incontinenza_fecale** | **int** | Richiedi o modifica identifier incontinenza fecale. | [optional] 
**id_incontenenza_urinaria** | **int** | Richiedi o modifica identifier incontenenza urinaria. | [optional] 
**note** | **str** | Richiedi o modifica note. | [optional] 
**id_analisi_bisogni_eliminazione** | **int** | Richiedi o modifica identifier analisi bisogni eliminazione. | [optional] 
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**id_visita** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dto_bisogni_paziente_eliminazione import DTOBisogniPazienteEliminazione

# TODO update the JSON string below
json = "{}"
# create an instance of DTOBisogniPazienteEliminazione from a JSON string
dto_bisogni_paziente_eliminazione_instance = DTOBisogniPazienteEliminazione.from_json(json)
# print the JSON string representation of the object
print DTOBisogniPazienteEliminazione.to_json()

# convert the object into a dict
dto_bisogni_paziente_eliminazione_dict = dto_bisogni_paziente_eliminazione_instance.to_dict()
# create an instance of DTOBisogniPazienteEliminazione from a dict
dto_bisogni_paziente_eliminazione_form_dict = dto_bisogni_paziente_eliminazione.from_dict(dto_bisogni_paziente_eliminazione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


