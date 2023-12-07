# ReportTypesGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReportTypesGet200ResponseDataInner]**](ReportTypesGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.report_types_get200_response import ReportTypesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReportTypesGet200Response from a JSON string
report_types_get200_response_instance = ReportTypesGet200Response.from_json(json)
# print the JSON string representation of the object
print ReportTypesGet200Response.to_json()

# convert the object into a dict
report_types_get200_response_dict = report_types_get200_response_instance.to_dict()
# create an instance of ReportTypesGet200Response from a dict
report_types_get200_response_form_dict = report_types_get200_response.from_dict(report_types_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


