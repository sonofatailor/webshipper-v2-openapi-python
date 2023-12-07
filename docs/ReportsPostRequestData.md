# ReportsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Reports**](Reports.md) |  | [optional] 

## Example

```python
from webshipperv2.models.reports_post_request_data import ReportsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ReportsPostRequestData from a JSON string
reports_post_request_data_instance = ReportsPostRequestData.from_json(json)
# print the JSON string representation of the object
print ReportsPostRequestData.to_json()

# convert the object into a dict
reports_post_request_data_dict = reports_post_request_data_instance.to_dict()
# create an instance of ReportsPostRequestData from a dict
reports_post_request_data_form_dict = reports_post_request_data.from_dict(reports_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


