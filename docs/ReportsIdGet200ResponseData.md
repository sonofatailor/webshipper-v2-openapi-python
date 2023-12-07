# ReportsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Reports**](Reports.md) |  | [optional] 

## Example

```python
from openapi_client.models.reports_id_get200_response_data import ReportsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ReportsIdGet200ResponseData from a JSON string
reports_id_get200_response_data_instance = ReportsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print ReportsIdGet200ResponseData.to_json()

# convert the object into a dict
reports_id_get200_response_data_dict = reports_id_get200_response_data_instance.to_dict()
# create an instance of ReportsIdGet200ResponseData from a dict
reports_id_get200_response_data_form_dict = reports_id_get200_response_data.from_dict(reports_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


