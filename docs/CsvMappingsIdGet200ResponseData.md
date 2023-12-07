# CsvMappingsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**CsvMappings**](CsvMappings.md) |  | [optional] 

## Example

```python
from openapi_client.models.csv_mappings_id_get200_response_data import CsvMappingsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CsvMappingsIdGet200ResponseData from a JSON string
csv_mappings_id_get200_response_data_instance = CsvMappingsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print CsvMappingsIdGet200ResponseData.to_json()

# convert the object into a dict
csv_mappings_id_get200_response_data_dict = csv_mappings_id_get200_response_data_instance.to_dict()
# create an instance of CsvMappingsIdGet200ResponseData from a dict
csv_mappings_id_get200_response_data_form_dict = csv_mappings_id_get200_response_data.from_dict(csv_mappings_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


