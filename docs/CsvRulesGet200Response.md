# CsvRulesGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CsvRulesGet200ResponseDataInner]**](CsvRulesGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.csv_rules_get200_response import CsvRulesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CsvRulesGet200Response from a JSON string
csv_rules_get200_response_instance = CsvRulesGet200Response.from_json(json)
# print the JSON string representation of the object
print CsvRulesGet200Response.to_json()

# convert the object into a dict
csv_rules_get200_response_dict = csv_rules_get200_response_instance.to_dict()
# create an instance of CsvRulesGet200Response from a dict
csv_rules_get200_response_form_dict = csv_rules_get200_response.from_dict(csv_rules_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


