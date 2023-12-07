# CsvMappingsIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | [**BarcodeRangesIdGet200ResponseRelationshipsCarrier**](BarcodeRangesIdGet200ResponseRelationshipsCarrier.md) |  | [optional] 
**order_channel** | [**CsvMappingsIdGet200ResponseRelationshipsOrderChannel**](CsvMappingsIdGet200ResponseRelationshipsOrderChannel.md) |  | [optional] 

## Example

```python
from openapi_client.models.csv_mappings_id_get200_response_relationships import CsvMappingsIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CsvMappingsIdGet200ResponseRelationships from a JSON string
csv_mappings_id_get200_response_relationships_instance = CsvMappingsIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print CsvMappingsIdGet200ResponseRelationships.to_json()

# convert the object into a dict
csv_mappings_id_get200_response_relationships_dict = csv_mappings_id_get200_response_relationships_instance.to_dict()
# create an instance of CsvMappingsIdGet200ResponseRelationships from a dict
csv_mappings_id_get200_response_relationships_form_dict = csv_mappings_id_get200_response_relationships.from_dict(csv_mappings_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


