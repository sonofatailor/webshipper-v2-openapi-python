# CsvUploadsPost204ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**CsvUploads**](CsvUploads.md) |  | [optional] 

## Example

```python
from openapi_client.models.csv_uploads_post204_response_data import CsvUploadsPost204ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CsvUploadsPost204ResponseData from a JSON string
csv_uploads_post204_response_data_instance = CsvUploadsPost204ResponseData.from_json(json)
# print the JSON string representation of the object
print CsvUploadsPost204ResponseData.to_json()

# convert the object into a dict
csv_uploads_post204_response_data_dict = csv_uploads_post204_response_data_instance.to_dict()
# create an instance of CsvUploadsPost204ResponseData from a dict
csv_uploads_post204_response_data_form_dict = csv_uploads_post204_response_data.from_dict(csv_uploads_post204_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


