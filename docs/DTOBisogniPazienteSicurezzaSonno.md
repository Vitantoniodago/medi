# DTOBisogniPazienteSicurezzaSonno



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alterazione_sonno** | **bool** | Richiedi o modifica un valore che indica [alterazione sonno]. | [optional] 
**allettato_con_sponde** | **bool** | Richiedi o modifica un valore che indica [allettato con sponde]. | [optional] 
**rischio_infezione** | **bool** | Richiedi o modifica un valore che indica [rischio infezione]. | [optional] 
**insonnia** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteSicurezzaSonno} is insonnia. | [optional] 
**infezione_in_atto** | **bool** | Richiedi o modifica un valore che indica [infezione in atto]. | [optional] 
**agitazione** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteSicurezzaSonno} is agitazione. | [optional] 
**malattia_contagiosa** | **bool** | Richiedi o modifica un valore che indica [malattia contagiosa]. | [optional] 
**defedamento** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteSicurezzaSonno} is defedamento. | [optional] 
**sovrappeso** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteSicurezzaSonno} is sovrappeso. | [optional] 
**rischio_caduta** | **bool** | Richiedi o modifica un valore che indica [rischio caduta]. | [optional] 
**note** | **str** | Richiedi o modifica note. | [optional] 
**id_analisi_bisogni_sicurezza_sonno** | **int** | Richiedi o modifica identifier analisi bisogni sicurezza sonno. | [optional] 
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**id_visita** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dto_bisogni_paziente_sicurezza_sonno import DTOBisogniPazienteSicurezzaSonno

# TODO update the JSON string below
json = "{}"
# create an instance of DTOBisogniPazienteSicurezzaSonno from a JSON string
dto_bisogni_paziente_sicurezza_sonno_instance = DTOBisogniPazienteSicurezzaSonno.from_json(json)
# print the JSON string representation of the object
print DTOBisogniPazienteSicurezzaSonno.to_json()

# convert the object into a dict
dto_bisogni_paziente_sicurezza_sonno_dict = dto_bisogni_paziente_sicurezza_sonno_instance.to_dict()
# create an instance of DTOBisogniPazienteSicurezzaSonno from a dict
dto_bisogni_paziente_sicurezza_sonno_form_dict = dto_bisogni_paziente_sicurezza_sonno.from_dict(dto_bisogni_paziente_sicurezza_sonno_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


