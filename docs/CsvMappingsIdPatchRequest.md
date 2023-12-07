# CsvMappingsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CsvMappingsIdGet200ResponseData**](CsvMappingsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**CsvMappingsIdGet200ResponseRelationships**](CsvMappingsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.csv_mappings_id_patch_request import CsvMappingsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CsvMappingsIdPatchRequest from a JSON string
csv_mappings_id_patch_request_instance = CsvMappingsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print CsvMappingsIdPatchRequest.to_json()

# convert the object into a dict
csv_mappings_id_patch_request_dict = csv_mappings_id_patch_request_instance.to_dict()
# create an instance of CsvMappingsIdPatchRequest from a dict
csv_mappings_id_patch_request_form_dict = csv_mappings_id_patch_request.from_dict(csv_mappings_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


