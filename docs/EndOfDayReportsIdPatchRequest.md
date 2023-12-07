# EndOfDayReportsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EndOfDayReportsIdGet200ResponseData**](EndOfDayReportsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**BarcodeRangesIdGet200ResponseRelationships**](BarcodeRangesIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.end_of_day_reports_id_patch_request import EndOfDayReportsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EndOfDayReportsIdPatchRequest from a JSON string
end_of_day_reports_id_patch_request_instance = EndOfDayReportsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print EndOfDayReportsIdPatchRequest.to_json()

# convert the object into a dict
end_of_day_reports_id_patch_request_dict = end_of_day_reports_id_patch_request_instance.to_dict()
# create an instance of EndOfDayReportsIdPatchRequest from a dict
end_of_day_reports_id_patch_request_form_dict = end_of_day_reports_id_patch_request.from_dict(end_of_day_reports_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


