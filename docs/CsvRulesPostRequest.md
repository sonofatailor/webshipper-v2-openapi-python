# CsvRulesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CsvRulesPostRequestData**](CsvRulesPostRequestData.md) |  | [optional] 
**relationships** | [**CsvRulesIdGet200ResponseRelationships**](CsvRulesIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.csv_rules_post_request import CsvRulesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CsvRulesPostRequest from a JSON string
csv_rules_post_request_instance = CsvRulesPostRequest.from_json(json)
# print the JSON string representation of the object
print CsvRulesPostRequest.to_json()

# convert the object into a dict
csv_rules_post_request_dict = csv_rules_post_request_instance.to_dict()
# create an instance of CsvRulesPostRequest from a dict
csv_rules_post_request_form_dict = csv_rules_post_request.from_dict(csv_rules_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


