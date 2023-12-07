# CsvMappingsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CsvMappingsPostRequestData**](CsvMappingsPostRequestData.md) |  | [optional] 
**relationships** | [**CsvMappingsIdGet200ResponseRelationships**](CsvMappingsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.csv_mappings_post_request import CsvMappingsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CsvMappingsPostRequest from a JSON string
csv_mappings_post_request_instance = CsvMappingsPostRequest.from_json(json)
# print the JSON string representation of the object
print CsvMappingsPostRequest.to_json()

# convert the object into a dict
csv_mappings_post_request_dict = csv_mappings_post_request_instance.to_dict()
# create an instance of CsvMappingsPostRequest from a dict
csv_mappings_post_request_form_dict = csv_mappings_post_request.from_dict(csv_mappings_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


