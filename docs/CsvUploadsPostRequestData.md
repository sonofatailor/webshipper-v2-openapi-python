# CsvUploadsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**CsvUploads**](CsvUploads.md) |  | [optional] 

## Example

```python
from webshipperv2.models.csv_uploads_post_request_data import CsvUploadsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CsvUploadsPostRequestData from a JSON string
csv_uploads_post_request_data_instance = CsvUploadsPostRequestData.from_json(json)
# print the JSON string representation of the object
print CsvUploadsPostRequestData.to_json()

# convert the object into a dict
csv_uploads_post_request_data_dict = csv_uploads_post_request_data_instance.to_dict()
# create an instance of CsvUploadsPostRequestData from a dict
csv_uploads_post_request_data_form_dict = csv_uploads_post_request_data.from_dict(csv_uploads_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


