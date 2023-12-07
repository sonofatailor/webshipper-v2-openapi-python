# CsvRulesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**CsvRules**](CsvRules.md) |  | [optional] 

## Example

```python
from webshipperv2.models.csv_rules_post_request_data import CsvRulesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CsvRulesPostRequestData from a JSON string
csv_rules_post_request_data_instance = CsvRulesPostRequestData.from_json(json)
# print the JSON string representation of the object
print CsvRulesPostRequestData.to_json()

# convert the object into a dict
csv_rules_post_request_data_dict = csv_rules_post_request_data_instance.to_dict()
# create an instance of CsvRulesPostRequestData from a dict
csv_rules_post_request_data_form_dict = csv_rules_post_request_data.from_dict(csv_rules_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


