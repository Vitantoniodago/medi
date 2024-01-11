# DTOAPIParametroPrestazione



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_parametro** | **int** | Richiedi o modifica identifier parametro. | [optional] 
**guid_prestazione** | **str** | Richiedi o modifica unique identifier prestazione. | [optional] 
**data_rilevazione** | **datetime** | Richiedi o modifica data rilevazione. | [optional] 
**id_tipo_dispositivo** | **int** | Richiedi o modifica identifier tipo dispositivo. | [optional] 
**id_tipo_dato** | **int** | Richiedi o modifica identifier tipo dato. | [optional] 
**valore** | **str** | Richiedi o modifica valore. | [optional] 

## Example

```python
from openapi_client.models.dtoapi_parametro_prestazione import DTOAPIParametroPrestazione

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIParametroPrestazione from a JSON string
dtoapi_parametro_prestazione_instance = DTOAPIParametroPrestazione.from_json(json)
# print the JSON string representation of the object
print DTOAPIParametroPrestazione.to_json()

# convert the object into a dict
dtoapi_parametro_prestazione_dict = dtoapi_parametro_prestazione_instance.to_dict()
# create an instance of DTOAPIParametroPrestazione from a dict
dtoapi_parametro_prestazione_form_dict = dtoapi_parametro_prestazione.from_dict(dtoapi_parametro_prestazione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


