# DTOBisogniPazienteAlimentazione



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assenza_alimentazione** | **bool** | Richiedi o modifica un valore che indica [assenza alimentazione]. | [optional] 
**alimentazione_orale** | **bool** | Richiedi o modifica un valore che indica [alimentazione orale]. | [optional] 
**ausili_alimentazione** | **bool** | Richiedi o modifica un valore che indica [ausili alimentazione]. | [optional] 
**imboccato** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteAlimentazione} is imboccato. | [optional] 
**dieta_specifica** | **bool** | Richiedi o modifica un valore che indica [dieta specifica]. | [optional] 
**dieta_sbilanciata** | **bool** | Richiedi o modifica un valore che indica [dieta sbilanciata]. | [optional] 
**ematemesi** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteAlimentazione} is ematemesi. | [optional] 
**meteorismo** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteAlimentazione} is meteorismo. | [optional] 
**protesi_dentaria** | **bool** | Richiedi o modifica un valore che indica [protesi dentaria]. | [optional] 
**nutrizione_parentale** | **bool** | Richiedi o modifica un valore che indica [nutrizione parentale]. | [optional] 
**nutrizione_enterale** | **bool** | Richiedi o modifica un valore che indica [nutrizione enterale]. | [optional] 
**melena** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteAlimentazione} is melena. | [optional] 
**sondino** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteAlimentazione} is sondino. | [optional] 
**rifiuto_cibo** | **bool** | Richiedi o modifica un valore che indica [rifiuto cibo]. | [optional] 
**calo_ponderale** | **bool** | Richiedi o modifica un valore che indica [calo ponderale]. | [optional] 
**id_gastrectomia** | **int** | Richiedi o modifica identifier gastrectomia. | [optional] 
**id_diabete** | **int** | Richiedi o modifica identifier diabete. | [optional] 
**intolleranze_alimentari** | **str** | Richiedi o modifica intolleranze alimentari. | [optional] 
**impedimento_alimentazione** | **str** | Richiedi o modifica impedimento alimentazione. | [optional] 
**note** | **str** | Richiedi o modifica note. | [optional] 
**id_analisi_bisogni_alimentazione** | **int** | Richiedi o modifica identifier analisi bisogni alimentazione. | [optional] 
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**id_visita** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dto_bisogni_paziente_alimentazione import DTOBisogniPazienteAlimentazione

# TODO update the JSON string below
json = "{}"
# create an instance of DTOBisogniPazienteAlimentazione from a JSON string
dto_bisogni_paziente_alimentazione_instance = DTOBisogniPazienteAlimentazione.from_json(json)
# print the JSON string representation of the object
print DTOBisogniPazienteAlimentazione.to_json()

# convert the object into a dict
dto_bisogni_paziente_alimentazione_dict = dto_bisogni_paziente_alimentazione_instance.to_dict()
# create an instance of DTOBisogniPazienteAlimentazione from a dict
dto_bisogni_paziente_alimentazione_form_dict = dto_bisogni_paziente_alimentazione.from_dict(dto_bisogni_paziente_alimentazione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


