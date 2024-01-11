# DTOAPIFattura


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_fatturazione** | **datetime** |  | [optional] 
**data_creazione** | **datetime** |  | [optional] 
**categoria_documento** | [**DTOAPICategoria**](DTOAPICategoria.md) |  | [optional] 
**codice_documento** | **str** |  | [optional] 
**mittente** | [**DTOAPIAzienda**](DTOAPIAzienda.md) |  | [optional] 
**destinatario** | [**DTOAPIAzienda**](DTOAPIAzienda.md) |  | [optional] 
**item_fattura** | [**List[DTOAPIFatturaItem]**](DTOAPIFatturaItem.md) |  | [optional] 
**sub_totale** | **float** |  | [optional] 
**totale_iva** | **float** |  | [optional] 
**totale_sconto** | **float** |  | [optional] 
**totale** | **float** |  | [optional] 
**note** | **str** |  | [optional] 
**stato_pagamento** | [**DTOAPICategoria**](DTOAPICategoria.md) |  | [optional] 
**tipologia_pagamento** | [**DTOAPICategoria**](DTOAPICategoria.md) |  | [optional] 
**condizioni_pagamento** | [**DTOAPICategoria**](DTOAPICategoria.md) |  | [optional] 
**assistito** | [**DTOAPIAnagrafica**](DTOAPIAnagrafica.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_fattura import DTOAPIFattura

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIFattura from a JSON string
dtoapi_fattura_instance = DTOAPIFattura.from_json(json)
# print the JSON string representation of the object
print DTOAPIFattura.to_json()

# convert the object into a dict
dtoapi_fattura_dict = dtoapi_fattura_instance.to_dict()
# create an instance of DTOAPIFattura from a dict
dtoapi_fattura_form_dict = dtoapi_fattura.from_dict(dtoapi_fattura_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


