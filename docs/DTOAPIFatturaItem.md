# DTOAPIFatturaItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prodotto** | [**DTOAPIProdotto**](DTOAPIProdotto.md) |  | [optional] 
**quantit_singolo** | **float** |  | [optional] 
**unita_qnt_singolo** | [**DTOAPIUnitaMisura**](DTOAPIUnitaMisura.md) |  | [optional] 
**tipologia_iva** | [**DTOAPICategoria**](DTOAPICategoria.md) |  | [optional] 
**esenzione_iva** | [**DTOAPICategoria**](DTOAPICategoria.md) |  | [optional] 
**prezzo_singolo** | **float** |  | [optional] 
**prezzo_totale** | **float** |  | [optional] 
**sconto** | **float** |  | [optional] 
**tipo_sconto** | **int** |  | [optional] 
**iva** | **float** |  | [optional] 
**codice_commerciale** | **str** |  | [optional] 
**nome_commerciale** | **str** |  | [optional] 
**tipo_retta_entita** | [**DTOAPICategoria**](DTOAPICategoria.md) |  | [optional] 
**mese** | **int** |  | [optional] 
**anno** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_fattura_item import DTOAPIFatturaItem

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIFatturaItem from a JSON string
dtoapi_fattura_item_instance = DTOAPIFatturaItem.from_json(json)
# print the JSON string representation of the object
print DTOAPIFatturaItem.to_json()

# convert the object into a dict
dtoapi_fattura_item_dict = dtoapi_fattura_item_instance.to_dict()
# create an instance of DTOAPIFatturaItem from a dict
dtoapi_fattura_item_form_dict = dtoapi_fattura_item.from_dict(dtoapi_fattura_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


