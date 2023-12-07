# CsvRulesIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**CsvRules**](CsvRules.md) |  | [optional] 

## Example

```python
from webshipperv2.models.csv_rules_id_get200_response_data import CsvRulesIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CsvRulesIdGet200ResponseData from a JSON string
csv_rules_id_get200_response_data_instance = CsvRulesIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print CsvRulesIdGet200ResponseData.to_json()

# convert the object into a dict
csv_rules_id_get200_response_data_dict = csv_rules_id_get200_response_data_instance.to_dict()
# create an instance of CsvRulesIdGet200ResponseData from a dict
csv_rules_id_get200_response_data_form_dict = csv_rules_id_get200_response_data.from_dict(csv_rules_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


