# ReportTypesIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**ReportTypes**](ReportTypes.md) |  | [optional] 

## Example

```python
from webshipperv2.models.report_types_id_get200_response_data import ReportTypesIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ReportTypesIdGet200ResponseData from a JSON string
report_types_id_get200_response_data_instance = ReportTypesIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print ReportTypesIdGet200ResponseData.to_json()

# convert the object into a dict
report_types_id_get200_response_data_dict = report_types_id_get200_response_data_instance.to_dict()
# create an instance of ReportTypesIdGet200ResponseData from a dict
report_types_id_get200_response_data_form_dict = report_types_id_get200_response_data.from_dict(report_types_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


