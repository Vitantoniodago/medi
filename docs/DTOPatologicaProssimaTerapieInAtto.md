# DTOPatologicaProssimaTerapieInAtto



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nessun_farmaco** | **bool** | Richiedi o modifica un valore che indica [nessun farmaco]. | [optional] 
**id_farmaco** | **int** |  | [optional] 
**quantita** | **str** | Richiedi o modifica quantita. | [optional] 
**frequenza_assunzione** | **int** | Richiedi o modifica frequenza assunzione. | [optional] 
**note** | **str** | Richiedi o modifica note. | [optional] 
**id_patologica_prossima_terapie_in_atto** | **int** | Richiedi o modifica identifier patologica prossima terapie in atto. | [optional] 
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**id_visita** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dto_patologica_prossima_terapie_in_atto import DTOPatologicaProssimaTerapieInAtto

# TODO update the JSON string below
json = "{}"
# create an instance of DTOPatologicaProssimaTerapieInAtto from a JSON string
dto_patologica_prossima_terapie_in_atto_instance = DTOPatologicaProssimaTerapieInAtto.from_json(json)
# print the JSON string representation of the object
print DTOPatologicaProssimaTerapieInAtto.to_json()

# convert the object into a dict
dto_patologica_prossima_terapie_in_atto_dict = dto_patologica_prossima_terapie_in_atto_instance.to_dict()
# create an instance of DTOPatologicaProssimaTerapieInAtto from a dict
dto_patologica_prossima_terapie_in_atto_form_dict = dto_patologica_prossima_terapie_in_atto.from_dict(dto_patologica_prossima_terapie_in_atto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


