# CsvMappingsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CsvMappingsGet200ResponseDataInner]**](CsvMappingsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.csv_mappings_get200_response import CsvMappingsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CsvMappingsGet200Response from a JSON string
csv_mappings_get200_response_instance = CsvMappingsGet200Response.from_json(json)
# print the JSON string representation of the object
print CsvMappingsGet200Response.to_json()

# convert the object into a dict
csv_mappings_get200_response_dict = csv_mappings_get200_response_instance.to_dict()
# create an instance of CsvMappingsGet200Response from a dict
csv_mappings_get200_response_form_dict = csv_mappings_get200_response.from_dict(csv_mappings_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


