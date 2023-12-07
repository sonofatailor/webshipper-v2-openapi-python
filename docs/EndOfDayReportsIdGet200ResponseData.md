# EndOfDayReportsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**EndOfDayReports**](EndOfDayReports.md) |  | [optional] 

## Example

```python
from openapi_client.models.end_of_day_reports_id_get200_response_data import EndOfDayReportsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of EndOfDayReportsIdGet200ResponseData from a JSON string
end_of_day_reports_id_get200_response_data_instance = EndOfDayReportsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print EndOfDayReportsIdGet200ResponseData.to_json()

# convert the object into a dict
end_of_day_reports_id_get200_response_data_dict = end_of_day_reports_id_get200_response_data_instance.to_dict()
# create an instance of EndOfDayReportsIdGet200ResponseData from a dict
end_of_day_reports_id_get200_response_data_form_dict = end_of_day_reports_id_get200_response_data.from_dict(end_of_day_reports_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


