# DTOSVICBudget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anno_budget** | **int** |  | [optional] 
**mese_budget** | **int** |  | [optional] 
**entrata_uscita** | **str** |  | [optional] 
**conto** | **int** |  | [optional] 
**sottoconto** | **int** |  | [optional] 
**descrizione** | **str** |  | [optional] 
**competenza** | **int** |  | [optional] 
**cassa** | **int** |  | [optional] 
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
from openapi_client.models.dtosvic_budget import DTOSVICBudget

# TODO update the JSON string below
json = "{}"
# create an instance of DTOSVICBudget from a JSON string
dtosvic_budget_instance = DTOSVICBudget.from_json(json)
# print the JSON string representation of the object
print DTOSVICBudget.to_json()

# convert the object into a dict
dtosvic_budget_dict = dtosvic_budget_instance.to_dict()
# create an instance of DTOSVICBudget from a dict
dtosvic_budget_form_dict = dtosvic_budget.from_dict(dtosvic_budget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


