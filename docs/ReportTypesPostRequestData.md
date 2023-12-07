# ReportTypesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**ReportTypes**](ReportTypes.md) |  | [optional] 

## Example

```python
from webshipperv2.models.report_types_post_request_data import ReportTypesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ReportTypesPostRequestData from a JSON string
report_types_post_request_data_instance = ReportTypesPostRequestData.from_json(json)
# print the JSON string representation of the object
print ReportTypesPostRequestData.to_json()

# convert the object into a dict
report_types_post_request_data_dict = report_types_post_request_data_instance.to_dict()
# create an instance of ReportTypesPostRequestData from a dict
report_types_post_request_data_form_dict = report_types_post_request_data.from_dict(report_types_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


