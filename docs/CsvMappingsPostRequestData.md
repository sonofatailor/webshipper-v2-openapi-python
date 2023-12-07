# CsvMappingsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**CsvMappings**](CsvMappings.md) |  | [optional] 

## Example

```python
from openapi_client.models.csv_mappings_post_request_data import CsvMappingsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CsvMappingsPostRequestData from a JSON string
csv_mappings_post_request_data_instance = CsvMappingsPostRequestData.from_json(json)
# print the JSON string representation of the object
print CsvMappingsPostRequestData.to_json()

# convert the object into a dict
csv_mappings_post_request_data_dict = csv_mappings_post_request_data_instance.to_dict()
# create an instance of CsvMappingsPostRequestData from a dict
csv_mappings_post_request_data_form_dict = csv_mappings_post_request_data.from_dict(csv_mappings_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


