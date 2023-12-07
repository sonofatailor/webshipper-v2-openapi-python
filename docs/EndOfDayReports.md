# EndOfDayReports


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_base64** | **str** | Base64 encoding of the PDF document. This must explicitly be included with fields[end_of_day_reports]&#x3D;&#39;base64&#39; | [optional] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**start_time** | **str** | Datetime representing the start time for the report | [optional] 
**end_time** | **str** | Datetime representing the end time for the report | [optional] 

## Example

```python
from webshipperv2.models.end_of_day_reports import EndOfDayReports

# TODO update the JSON string below
json = "{}"
# create an instance of EndOfDayReports from a JSON string
end_of_day_reports_instance = EndOfDayReports.from_json(json)
# print the JSON string representation of the object
print EndOfDayReports.to_json()

# convert the object into a dict
end_of_day_reports_dict = end_of_day_reports_instance.to_dict()
# create an instance of EndOfDayReports from a dict
end_of_day_reports_form_dict = end_of_day_reports.from_dict(end_of_day_reports_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


