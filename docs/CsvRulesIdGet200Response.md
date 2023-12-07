# CsvRulesIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CsvRulesIdGet200ResponseData**](CsvRulesIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**CsvRulesIdGet200ResponseRelationships**](CsvRulesIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[CsvRulesIdGet200ResponseIncludedInner]**](CsvRulesIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.csv_rules_id_get200_response import CsvRulesIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CsvRulesIdGet200Response from a JSON string
csv_rules_id_get200_response_instance = CsvRulesIdGet200Response.from_json(json)
# print the JSON string representation of the object
print CsvRulesIdGet200Response.to_json()

# convert the object into a dict
csv_rules_id_get200_response_dict = csv_rules_id_get200_response_instance.to_dict()
# create an instance of CsvRulesIdGet200Response from a dict
csv_rules_id_get200_response_form_dict = csv_rules_id_get200_response.from_dict(csv_rules_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


