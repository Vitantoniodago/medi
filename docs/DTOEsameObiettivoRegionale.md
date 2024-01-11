# DTOEsameObiettivoRegionale



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**id_esame_obiettivo_regionale** | **int** | Richiedi o modifica identifier esame obiettivo regionale. | [optional] 
**idmv_polmone_destro** | **str** | Richiedi o modifica idmv polmone destro. | [optional] 
**idfvt_polmone_destro** | **str** | Richiedi o modifica idfvt polmone destro. | [optional] 
**id_percussione_polmone_destro** | **str** | Richiedi o modifica identifier percussione polmone destro. | [optional] 
**id_rumori_patologici_polmone_destro** | **str** | Richiedi o modifica identifier rumori patologici polmone destro. | [optional] 
**id_sede_polmone_destro** | **str** | Richiedi o modifica identifier sede polmone destro. | [optional] 
**idmv_polmone_sinistro** | **str** | Richiedi o modifica idmv polmone sinistro. | [optional] 
**idfvt_polmone_sinistro** | **str** | Richiedi o modifica idfvt polmone sinistro. | [optional] 
**id_percussione_polmone_sinistro** | **str** | Richiedi o modifica identifier percussione polmone sinistro. | [optional] 
**id_rumori_patologici_polmone_sinistro** | **str** | Richiedi o modifica identifier rumori patologici polmone sinistro. | [optional] 
**id_sede_polmone_sinistro** | **str** | Richiedi o modifica identifier sede polmone sinistro. | [optional] 
**id_tono** | **str** | Richiedi o modifica identifier tono. | [optional] 
**id_soffi** | **str** | Richiedi o modifica identifier soffi. | [optional] 
**id_apparato_urogenitale** | **str** | Richiedi o modifica identifier apparato urogenitale. | [optional] 
**id_addome** | **str** | Richiedi o modifica identifier addome. | [optional] 
**id_occhi** | **int** |  | [optional] 
**id_vista** | **int** |  | [optional] 
**note_vista** | **str** |  | [optional] 
**id_cavo_orale** | **int** |  | [optional] 
**orecchio** | **str** |  | [optional] 
**id_udito** | **int** |  | [optional] 
**note_udito** | **str** |  | [optional] 
**id_collo** | **int** |  | [optional] 
**sistema_arterioso** | **str** |  | [optional] 
**sistema_venoso_linfatico** | **str** |  | [optional] 
**apparato_muscolo_scheletrico** | **str** |  | [optional] 
**alterazione_podologica** | **str** |  | [optional] 
**id_tono_sistema_nervoso** | **int** |  | [optional] 
**note_tono_sistema_nervoso** | **str** |  | [optional] 
**id_movimenti** | **int** |  | [optional] 
**id_visita** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dto_esame_obiettivo_regionale import DTOEsameObiettivoRegionale

# TODO update the JSON string below
json = "{}"
# create an instance of DTOEsameObiettivoRegionale from a JSON string
dto_esame_obiettivo_regionale_instance = DTOEsameObiettivoRegionale.from_json(json)
# print the JSON string representation of the object
print DTOEsameObiettivoRegionale.to_json()

# convert the object into a dict
dto_esame_obiettivo_regionale_dict = dto_esame_obiettivo_regionale_instance.to_dict()
# create an instance of DTOEsameObiettivoRegionale from a dict
dto_esame_obiettivo_regionale_form_dict = dto_esame_obiettivo_regionale.from_dict(dto_esame_obiettivo_regionale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


