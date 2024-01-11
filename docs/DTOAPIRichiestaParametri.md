# DTOAPIRichiestaParametri



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid_prestazione** | **str** | Richiedi o modifica unique identifier prestazione. | [optional] 
**id_ultimo_parametro** | **int** | Richiedi o modifica identifier ultimo parametro. | [optional] 
**id_tipologia_dispositivo** | **int** | Richiedi o modifica identifier tipologia dispositivo. | [optional] 
**id_tipologia_dato** | **int** | Richiedi o modifica identifier tipologia dato. | [optional] 

## Example

```python
from openapi_client.models.dtoapi_richiesta_parametri import DTOAPIRichiestaParametri

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIRichiestaParametri from a JSON string
dtoapi_richiesta_parametri_instance = DTOAPIRichiestaParametri.from_json(json)
# print the JSON string representation of the object
print DTOAPIRichiestaParametri.to_json()

# convert the object into a dict
dtoapi_richiesta_parametri_dict = dtoapi_richiesta_parametri_instance.to_dict()
# create an instance of DTOAPIRichiestaParametri from a dict
dtoapi_richiesta_parametri_form_dict = dtoapi_richiesta_parametri.from_dict(dtoapi_richiesta_parametri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


