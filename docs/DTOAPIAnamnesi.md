# DTOAPIAnamnesi



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anamnesi_familiare** | [**List[DTOAnamnesiFamiliare]**](DTOAnamnesiFamiliare.md) |  | [optional] 
**patologica_prossima_terapia** | [**List[DTOPatologicaProssimaTerapieInAtto]**](DTOPatologicaProssimaTerapieInAtto.md) |  | [optional] 
**patologica_prossima_ulcere** | [**List[DTOPatologicaProssimaUlcereDaPressione]**](DTOPatologicaProssimaUlcereDaPressione.md) |  | [optional] 
**patologica_remota_interventi_pregressi** | [**List[DTOPatologicaRemotaInterventiPregressi]**](DTOPatologicaRemotaInterventiPregressi.md) |  | [optional] 
**patologica_remota_malattie** | [**List[DTOPatologicaRemotaMalattie]**](DTOPatologicaRemotaMalattie.md) |  | [optional] 
**patologica_remota_ricoveri_pregressi** | [**List[DTOPatologicaRemotaRicoveriPregressi]**](DTOPatologicaRemotaRicoveriPregressi.md) |  | [optional] 

## Example

```python
from openapi_client.models.dtoapi_anamnesi import DTOAPIAnamnesi

# TODO update the JSON string below
json = "{}"
# create an instance of DTOAPIAnamnesi from a JSON string
dtoapi_anamnesi_instance = DTOAPIAnamnesi.from_json(json)
# print the JSON string representation of the object
print DTOAPIAnamnesi.to_json()

# convert the object into a dict
dtoapi_anamnesi_dict = dtoapi_anamnesi_instance.to_dict()
# create an instance of DTOAPIAnamnesi from a dict
dtoapi_anamnesi_form_dict = dtoapi_anamnesi.from_dict(dtoapi_anamnesi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


