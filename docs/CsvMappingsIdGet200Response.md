# CsvMappingsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CsvMappingsIdGet200ResponseData**](CsvMappingsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**CsvMappingsIdGet200ResponseRelationships**](CsvMappingsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[CsvMappingsIdGet200ResponseIncludedInner]**](CsvMappingsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.csv_mappings_id_get200_response import CsvMappingsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CsvMappingsIdGet200Response from a JSON string
csv_mappings_id_get200_response_instance = CsvMappingsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print CsvMappingsIdGet200Response.to_json()

# convert the object into a dict
csv_mappings_id_get200_response_dict = csv_mappings_id_get200_response_instance.to_dict()
# create an instance of CsvMappingsIdGet200Response from a dict
csv_mappings_id_get200_response_form_dict = csv_mappings_id_get200_response.from_dict(csv_mappings_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


