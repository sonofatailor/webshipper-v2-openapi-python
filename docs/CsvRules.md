# CsvRules


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_path** | **str** | Path of the attribute to update | [optional] 
**source_index** | **int** | The index of the field in the CSV file to be mapped | [optional] 
**default_value** | **str** | Value to use if the value in the CSV file is empty or missing | [optional] 
**input_conversions** | **object** | A key/value mapping for converting values before creating the object | [optional] 

## Example

```python
from openapi_client.models.csv_rules import CsvRules

# TODO update the JSON string below
json = "{}"
# create an instance of CsvRules from a JSON string
csv_rules_instance = CsvRules.from_json(json)
# print the JSON string representation of the object
print CsvRules.to_json()

# convert the object into a dict
csv_rules_dict = csv_rules_instance.to_dict()
# create an instance of CsvRules from a dict
csv_rules_form_dict = csv_rules.from_dict(csv_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


