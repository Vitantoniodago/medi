# DTOItemPrestazioni



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_item_prestazione** | **int** | Richiedi o modifica identifier item prestazione. | [optional] 
**id_prestazione** | **int** | Richiedi o modifica identifier prestazione. | [optional] 
**time_start** | **datetime** | Richiedi o modifica time start. | [optional] 
**time_end** | **datetime** | Richiedi o modifica time end. | [optional] 
**lunedi** | **bool** | Richiedi o modifica lunedi. | [optional] 
**martedi** | **bool** | Richiedi o modifica martedi. | [optional] 
**mercoledi** | **bool** | Richiedi o modifica mercoledi. | [optional] 
**giovedi** | **bool** | Richiedi o modifica giovedi. | [optional] 
**venerdi** | **bool** | Richiedi o modifica venerdi. | [optional] 
**sabato** | **bool** | Richiedi o modifica sabato. | [optional] 
**domenica** | **bool** | Richiedi o modifica domenica. | [optional] 

## Example

```python
from openapi_client.models.dto_item_prestazioni import DTOItemPrestazioni

# TODO update the JSON string below
json = "{}"
# create an instance of DTOItemPrestazioni from a JSON string
dto_item_prestazioni_instance = DTOItemPrestazioni.from_json(json)
# print the JSON string representation of the object
print DTOItemPrestazioni.to_json()

# convert the object into a dict
dto_item_prestazioni_dict = dto_item_prestazioni_instance.to_dict()
# create an instance of DTOItemPrestazioni from a dict
dto_item_prestazioni_form_dict = dto_item_prestazioni.from_dict(dto_item_prestazioni_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


