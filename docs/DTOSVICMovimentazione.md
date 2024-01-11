# DTOSVICMovimentazione


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tipo_operazione** | **str** |  | [optional] 
**data_operazione** | **datetime** |  | [optional] 
**numero_operazione** | **int** |  | [optional] 
**conto** | **int** |  | [optional] 
**sottoconto** | **int** |  | [optional] 
**dare_avere** | **str** |  | [optional] 
**importo** | **int** |  | [optional] 
**missione** | **int** |  | [optional] 
**descrizione_missione** | **str** |  | [optional] 
**programma** | **int** |  | [optional] 
**descrizione_programma** | **str** |  | [optional] 
**titolo** | **int** |  | [optional] 
**descrizione_titolo** | **str** |  | [optional] 
**responsabile** | **str** |  | [optional] 
**contro_di_costo_ricavo** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dtosvic_movimentazione import DTOSVICMovimentazione

# TODO update the JSON string below
json = "{}"
# create an instance of DTOSVICMovimentazione from a JSON string
dtosvic_movimentazione_instance = DTOSVICMovimentazione.from_json(json)
# print the JSON string representation of the object
print DTOSVICMovimentazione.to_json()

# convert the object into a dict
dtosvic_movimentazione_dict = dtosvic_movimentazione_instance.to_dict()
# create an instance of DTOSVICMovimentazione from a dict
dtosvic_movimentazione_form_dict = dtosvic_movimentazione.from_dict(dtosvic_movimentazione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


