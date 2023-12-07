# ReportTypesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReportTypesPostRequestData**](ReportTypesPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.report_types_post_request import ReportTypesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportTypesPostRequest from a JSON string
report_types_post_request_instance = ReportTypesPostRequest.from_json(json)
# print the JSON string representation of the object
print ReportTypesPostRequest.to_json()

# convert the object into a dict
report_types_post_request_dict = report_types_post_request_instance.to_dict()
# create an instance of ReportTypesPostRequest from a dict
report_types_post_request_form_dict = report_types_post_request.from_dict(report_types_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


