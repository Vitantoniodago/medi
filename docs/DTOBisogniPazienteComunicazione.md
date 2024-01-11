# DTOBisogniPazienteComunicazione



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assenza_comunicazione** | **bool** | Richiedi o modifica un valore che indica [assenza comunicazione]. | [optional] 
**disturbi_uditivi** | **bool** | Richiedi o modifica un valore che indica [disturbi uditivi]. | [optional] 
**difficolta_comunicazione** | **bool** | Richiedi o modifica un valore che indica [difficolta comunicazione]. | [optional] 
**sordomutismo** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteComunicazione} is sordomutismo. | [optional] 
**sensorio_obnubilato** | **bool** | Richiedi o modifica un valore che indica [sensorio obnubilato]. | [optional] 
**trachestomia** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteComunicazione} is trachestomia. | [optional] 
**cecita_bilaterale** | **bool** | Richiedi o modifica un valore che indica [cecita bilaterale]. | [optional] 
**stato_soporoso** | **bool** | Richiedi o modifica un valore che indica [stato soporoso]. | [optional] 
**portatore_lenti** | **bool** | Richiedi o modifica un valore che indica [portatore lenti]. | [optional] 
**stato_coma** | **bool** | Richiedi o modifica un valore che indica [stato coma]. | [optional] 
**glaucoma** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteComunicazione} is glaucoma. | [optional] 
**mancanza_conoscenza_malattia** | **bool** | Richiedi o modifica un valore che indica [mancanza conoscenza malattia]. | [optional] 
**congiuntivite** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteComunicazione} is congiuntivite. | [optional] 
**preoccupazione_stato** | **bool** | Richiedi o modifica un valore che indica [preoccupazione stato]. | [optional] 
**otalgie** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteComunicazione} is otalgie. | [optional] 
**rapporto_difficile_parenti** | **bool** | Richiedi o modifica un valore che indica [rapporto difficile parenti]. | [optional] 
**sordita_bilaterale** | **bool** | Richiedi o modifica un valore che indica [sordita bilaterale]. | [optional] 
**preoccupazione_lavoro** | **bool** | Richiedi o modifica un valore che indica [preoccupazione lavoro]. | [optional] 
**protesi_fonetica** | **bool** | Richiedi o modifica un valore che indica [protesi fonetica]. | [optional] 
**tossicodipendenza** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteComunicazione} is tossicodipendenza. | [optional] 
**protesi_acustica** | **bool** | Richiedi o modifica un valore che indica [protesi acustica]. | [optional] 
**alcoldipendenza** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteComunicazione} is alcoldipendenza. | [optional] 
**disturbi_linguaggio** | **bool** | Richiedi o modifica un valore che indica [disturbi linguaggio]. | [optional] 
**stati_psicologici** | **str** | Richiedi o modifica stati psicologici. | [optional] 
**alterazione_umore** | **str** | Richiedi o modifica alterazione umore. | [optional] 
**note** | **str** | Richiedi o modifica note. | [optional] 
**id_analisi_bisogni_comunicazione** | **int** | Richiedi o modifica identifier analisi bisogni comunicazione. | [optional] 
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**id_visita** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dto_bisogni_paziente_comunicazione import DTOBisogniPazienteComunicazione

# TODO update the JSON string below
json = "{}"
# create an instance of DTOBisogniPazienteComunicazione from a JSON string
dto_bisogni_paziente_comunicazione_instance = DTOBisogniPazienteComunicazione.from_json(json)
# print the JSON string representation of the object
print DTOBisogniPazienteComunicazione.to_json()

# convert the object into a dict
dto_bisogni_paziente_comunicazione_dict = dto_bisogni_paziente_comunicazione_instance.to_dict()
# create an instance of DTOBisogniPazienteComunicazione from a dict
dto_bisogni_paziente_comunicazione_form_dict = dto_bisogni_paziente_comunicazione.from_dict(dto_bisogni_paziente_comunicazione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


