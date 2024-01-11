# DTOEsameObiettivoGenerale



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_visita** | **datetime** | Richiedi o modifica data visita. | [optional] 
**altezza** | **float** | Richiedi o modifica altezza. | [optional] 
**peso** | **float** | Richiedi o modifica peso. | [optional] 
**bmi** | **float** | Richiedi o modifica bmi. | [optional] 
**stato_nutrizione** | **str** | Richiedi o modifica stato nutrizione. | [optional] 
**circonferenza_addominale** | **float** | Richiedi o modifica circonferenza addominale. | [optional] 
**temperatura** | **float** | Richiedi o modifica temperatura. | [optional] 
**id_localizzazione_temperatura** | **int** | Richiedi o modifica identifier localizzazione temperatura. | [optional] 
**pa_sistolica** | **float** | Richiedi o modifica pa sistolica. | [optional] 
**pa_diastolica** | **float** | Richiedi o modifica pa diastolica. | [optional] 
**freq_respiro** | **float** | Richiedi o modifica freq respiro. | [optional] 
**freq_cardiaca** | **float** | Richiedi o modifica freq cardiaca. | [optional] 
**id_stato_generale** | **str** | Richiedi o modifica identifier stato generale. | [optional] 
**note** | **str** | Richiedi o modifica note. | [optional] 
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**id_esame_obiettivo_generale** | **int** | Richiedi o modifica identifier esame obiettivo generale. | [optional] 
**id_decubito** | **str** | Richiedi o modifica identifier decubito. | [optional] 
**id_mucose** | **str** | Richiedi o modifica identifier mucose. | [optional] 
**id_masse_muscolari** | **str** | Richiedi o modifica identifier masse muscolari. | [optional] 
**id_polso** | **str** | Richiedi o modifica identifier polso. | [optional] 
**id_stato_psichico** | **str** | Richiedi o modifica identifier stato psichico. | [optional] 
**id_cute** | **str** | Richiedi o modifica identifier cute. | [optional] 
**id_sottocute** | **str** | Richiedi o modifica identifier sottocute. | [optional] 
**id_lingua** | **str** | Richiedi o modifica identifier lingua. | [optional] 
**id_respiro** | **str** | Richiedi o modifica identifier respiro. | [optional] 
**id_visita** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dto_esame_obiettivo_generale import DTOEsameObiettivoGenerale

# TODO update the JSON string below
json = "{}"
# create an instance of DTOEsameObiettivoGenerale from a JSON string
dto_esame_obiettivo_generale_instance = DTOEsameObiettivoGenerale.from_json(json)
# print the JSON string representation of the object
print DTOEsameObiettivoGenerale.to_json()

# convert the object into a dict
dto_esame_obiettivo_generale_dict = dto_esame_obiettivo_generale_instance.to_dict()
# create an instance of DTOEsameObiettivoGenerale from a dict
dto_esame_obiettivo_generale_form_dict = dto_esame_obiettivo_generale.from_dict(dto_esame_obiettivo_generale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


