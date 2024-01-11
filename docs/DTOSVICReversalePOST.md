# DTOSVICReversalePOST


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_accertamento** | **str** |  | [optional] 
**anno_pagamento** | **int** |  | [optional] 
**anno_competenza** | **int** |  | [optional] 
**dettaglio** | [**List[DTOSVICRigaReversale]**](DTOSVICRigaReversale.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtosvic_reversale_post import DTOSVICReversalePOST

# TODO update the JSON string below
json = "{}"
# create an instance of DTOSVICReversalePOST from a JSON string
dtosvic_reversale_post_instance = DTOSVICReversalePOST.from_json(json)
# print the JSON string representation of the object
print DTOSVICReversalePOST.to_json()

# convert the object into a dict
dtosvic_reversale_post_dict = dtosvic_reversale_post_instance.to_dict()
# create an instance of DTOSVICReversalePOST from a dict
dtosvic_reversale_post_form_dict = dtosvic_reversale_post.from_dict(dtosvic_reversale_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


