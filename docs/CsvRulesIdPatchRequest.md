# CsvRulesIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CsvRulesIdGet200ResponseData**](CsvRulesIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**CsvRulesIdGet200ResponseRelationships**](CsvRulesIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.csv_rules_id_patch_request import CsvRulesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CsvRulesIdPatchRequest from a JSON string
csv_rules_id_patch_request_instance = CsvRulesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print CsvRulesIdPatchRequest.to_json()

# convert the object into a dict
csv_rules_id_patch_request_dict = csv_rules_id_patch_request_instance.to_dict()
# create an instance of CsvRulesIdPatchRequest from a dict
csv_rules_id_patch_request_form_dict = csv_rules_id_patch_request.from_dict(csv_rules_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


