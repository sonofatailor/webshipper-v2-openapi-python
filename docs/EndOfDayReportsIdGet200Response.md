# EndOfDayReportsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EndOfDayReportsIdGet200ResponseData**](EndOfDayReportsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**BarcodeRangesIdGet200ResponseRelationships**](BarcodeRangesIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[BarcodeRangesIdGet200ResponseIncludedInner]**](BarcodeRangesIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.end_of_day_reports_id_get200_response import EndOfDayReportsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EndOfDayReportsIdGet200Response from a JSON string
end_of_day_reports_id_get200_response_instance = EndOfDayReportsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print EndOfDayReportsIdGet200Response.to_json()

# convert the object into a dict
end_of_day_reports_id_get200_response_dict = end_of_day_reports_id_get200_response_instance.to_dict()
# create an instance of EndOfDayReportsIdGet200Response from a dict
end_of_day_reports_id_get200_response_form_dict = end_of_day_reports_id_get200_response.from_dict(end_of_day_reports_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


