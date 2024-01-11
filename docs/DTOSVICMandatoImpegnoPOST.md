# DTOSVICMandatoImpegnoPOST


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_impegno** | **str** |  | [optional] 
**anno_pagamento** | **int** |  | [optional] 
**anno_competenza** | **int** |  | [optional] 
**anno_assunzione** | **int** |  | [optional] 
**dettaglio** | [**List[DTOSVICRigaMandato]**](DTOSVICRigaMandato.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtosvic_mandato_impegno_post import DTOSVICMandatoImpegnoPOST

# TODO update the JSON string below
json = "{}"
# create an instance of DTOSVICMandatoImpegnoPOST from a JSON string
dtosvic_mandato_impegno_post_instance = DTOSVICMandatoImpegnoPOST.from_json(json)
# print the JSON string representation of the object
print DTOSVICMandatoImpegnoPOST.to_json()

# convert the object into a dict
dtosvic_mandato_impegno_post_dict = dtosvic_mandato_impegno_post_instance.to_dict()
# create an instance of DTOSVICMandatoImpegnoPOST from a dict
dtosvic_mandato_impegno_post_form_dict = dtosvic_mandato_impegno_post.from_dict(dtosvic_mandato_impegno_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


