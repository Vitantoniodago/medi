# DTOSVICMandatoSpesaFissaPOST


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capitolo** | **str** |  | [optional] 
**articolo** | **str** |  | [optional] 
**causale** | **str** |  | [optional] 
**anno_pagamento** | **int** |  | [optional] 
**anno_competenza** | **int** |  | [optional] 
**dettaglio** | [**List[DTOSVICRigaMandato]**](DTOSVICRigaMandato.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtosvic_mandato_spesa_fissa_post import DTOSVICMandatoSpesaFissaPOST

# TODO update the JSON string below
json = "{}"
# create an instance of DTOSVICMandatoSpesaFissaPOST from a JSON string
dtosvic_mandato_spesa_fissa_post_instance = DTOSVICMandatoSpesaFissaPOST.from_json(json)
# print the JSON string representation of the object
print DTOSVICMandatoSpesaFissaPOST.to_json()

# convert the object into a dict
dtosvic_mandato_spesa_fissa_post_dict = dtosvic_mandato_spesa_fissa_post_instance.to_dict()
# create an instance of DTOSVICMandatoSpesaFissaPOST from a dict
dtosvic_mandato_spesa_fissa_post_form_dict = dtosvic_mandato_spesa_fissa_post.from_dict(dtosvic_mandato_spesa_fissa_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


