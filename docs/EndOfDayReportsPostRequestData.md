# EndOfDayReportsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**EndOfDayReports**](EndOfDayReports.md) |  | [optional] 

## Example

```python
from webshipperv2.models.end_of_day_reports_post_request_data import EndOfDayReportsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of EndOfDayReportsPostRequestData from a JSON string
end_of_day_reports_post_request_data_instance = EndOfDayReportsPostRequestData.from_json(json)
# print the JSON string representation of the object
print EndOfDayReportsPostRequestData.to_json()

# convert the object into a dict
end_of_day_reports_post_request_data_dict = end_of_day_reports_post_request_data_instance.to_dict()
# create an instance of EndOfDayReportsPostRequestData from a dict
end_of_day_reports_post_request_data_form_dict = end_of_day_reports_post_request_data.from_dict(end_of_day_reports_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


