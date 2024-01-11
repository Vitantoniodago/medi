# DTOPatologicaProssimaUlcereDaPressione



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**sede** | **str** | Richiedi o modifica sede. | [optional] 
**id_grado** | **int** | Richiedi o modifica identifier grado. | [optional] 
**medicazione** | **str** | Richiedi o modifica medicazione. | [optional] 
**id_patologica_prossima_ulcere_da_pressione** | **int** | Richiedi o modifica identifier patologica prossima ulcere da pressione. | [optional] 
**id_visita** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dto_patologica_prossima_ulcere_da_pressione import DTOPatologicaProssimaUlcereDaPressione

# TODO update the JSON string below
json = "{}"
# create an instance of DTOPatologicaProssimaUlcereDaPressione from a JSON string
dto_patologica_prossima_ulcere_da_pressione_instance = DTOPatologicaProssimaUlcereDaPressione.from_json(json)
# print the JSON string representation of the object
print DTOPatologicaProssimaUlcereDaPressione.to_json()

# convert the object into a dict
dto_patologica_prossima_ulcere_da_pressione_dict = dto_patologica_prossima_ulcere_da_pressione_instance.to_dict()
# create an instance of DTOPatologicaProssimaUlcereDaPressione from a dict
dto_patologica_prossima_ulcere_da_pressione_form_dict = dto_patologica_prossima_ulcere_da_pressione.from_dict(dto_patologica_prossima_ulcere_da_pressione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


