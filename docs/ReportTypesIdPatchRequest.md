# ReportTypesIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReportTypesIdGet200ResponseData**](ReportTypesIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.report_types_id_patch_request import ReportTypesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportTypesIdPatchRequest from a JSON string
report_types_id_patch_request_instance = ReportTypesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ReportTypesIdPatchRequest.to_json()

# convert the object into a dict
report_types_id_patch_request_dict = report_types_id_patch_request_instance.to_dict()
# create an instance of ReportTypesIdPatchRequest from a dict
report_types_id_patch_request_form_dict = report_types_id_patch_request.from_dict(report_types_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


