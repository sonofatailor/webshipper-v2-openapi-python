# ReportsIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_type** | [**ReportsIdGet200ResponseRelationshipsReportType**](ReportsIdGet200ResponseRelationshipsReportType.md) |  | [optional] 
**carrier** | [**BarcodeRangesIdGet200ResponseRelationshipsCarrier**](BarcodeRangesIdGet200ResponseRelationshipsCarrier.md) |  | [optional] 

## Example

```python
from openapi_client.models.reports_id_get200_response_relationships import ReportsIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ReportsIdGet200ResponseRelationships from a JSON string
reports_id_get200_response_relationships_instance = ReportsIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print ReportsIdGet200ResponseRelationships.to_json()

# convert the object into a dict
reports_id_get200_response_relationships_dict = reports_id_get200_response_relationships_instance.to_dict()
# create an instance of ReportsIdGet200ResponseRelationships from a dict
reports_id_get200_response_relationships_form_dict = reports_id_get200_response_relationships.from_dict(reports_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


