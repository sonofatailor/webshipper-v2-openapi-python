# ReportsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReportsIdGet200ResponseData**](ReportsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**ReportsIdGet200ResponseRelationships**](ReportsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.reports_id_patch_request import ReportsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportsIdPatchRequest from a JSON string
reports_id_patch_request_instance = ReportsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ReportsIdPatchRequest.to_json()

# convert the object into a dict
reports_id_patch_request_dict = reports_id_patch_request_instance.to_dict()
# create an instance of ReportsIdPatchRequest from a dict
reports_id_patch_request_form_dict = reports_id_patch_request.from_dict(reports_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


