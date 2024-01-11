# DTOAnamnesiFamiliare



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_anamnesi_familiare** | **int** | Richiedi o modifica identifier anamnesi familiare. | [optional] 
**nega_presenza_patologia** | **bool** | Richiedi o modifica un valore che indica [nega presenza patologia]. | [optional] 
**id_parentela** | **int** | Richiedi o modifica identifier parentela. | [optional] 
**id_diagnosi** | **int** | Richiedi o modifica identifier diagnosi. | [optional] 
**deceduto** | **bool** | Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOAnamnesiFamiliare} is deceduto. | [optional] 
**note** | **str** | Richiedi o modifica note. | [optional] 
**id_assistito** | **int** | Richiedi o modifica identifier assistito. | [optional] 
**eta** | **int** | Richiedi o modifica eta. | [optional] 
**id_ereditarieta** | **int** | Richiedi o modifica identifier ereditarieta. | [optional] 
**id_visita** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dto_anamnesi_familiare import DTOAnamnesiFamiliare

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAnamnesiFamiliare from a JSON string
dto_anamnesi_familiare_instance = DTOAnamnesiFamiliare.from_json(json)
# print the JSON string representation of the object
print DTOAnamnesiFamiliare.to_json()

# convert the object into a dict
dto_anamnesi_familiare_dict = dto_anamnesi_familiare_instance.to_dict()
# create an instance of DTOAnamnesiFamiliare from a dict
dto_anamnesi_familiare_form_dict = dto_anamnesi_familiare.from_dict(dto_anamnesi_familiare_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


