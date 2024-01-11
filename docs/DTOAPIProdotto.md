# DTOAPIProdotto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nome_prodotto** | **str** |  | [optional] 
**categoria** | [**DTOAPICategoria**](DTOAPICategoria.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_prodotto import DTOAPIProdotto

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIProdotto from a JSON string
dtoapi_prodotto_instance = DTOAPIProdotto.from_json(json)
# print the JSON string representation of the object
print DTOAPIProdotto.to_json()

# convert the object into a dict
dtoapi_prodotto_dict = dtoapi_prodotto_instance.to_dict()
# create an instance of DTOAPIProdotto from a dict
dtoapi_prodotto_form_dict = dtoapi_prodotto.from_dict(dtoapi_prodotto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


