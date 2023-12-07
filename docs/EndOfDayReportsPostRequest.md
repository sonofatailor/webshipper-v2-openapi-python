# EndOfDayReportsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EndOfDayReportsPostRequestData**](EndOfDayReportsPostRequestData.md) |  | [optional] 
**relationships** | [**BarcodeRangesIdGet200ResponseRelationships**](BarcodeRangesIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.end_of_day_reports_post_request import EndOfDayReportsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EndOfDayReportsPostRequest from a JSON string
end_of_day_reports_post_request_instance = EndOfDayReportsPostRequest.from_json(json)
# print the JSON string representation of the object
print EndOfDayReportsPostRequest.to_json()

# convert the object into a dict
end_of_day_reports_post_request_dict = end_of_day_reports_post_request_instance.to_dict()
# create an instance of EndOfDayReportsPostRequest from a dict
end_of_day_reports_post_request_form_dict = end_of_day_reports_post_request.from_dict(end_of_day_reports_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


