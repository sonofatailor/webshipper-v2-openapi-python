# CsvUploadsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CsvUploadsPostRequestData**](CsvUploadsPostRequestData.md) |  | [optional] 
**relationships** | [**CsvRulesIdGet200ResponseRelationships**](CsvRulesIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.csv_uploads_post_request import CsvUploadsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CsvUploadsPostRequest from a JSON string
csv_uploads_post_request_instance = CsvUploadsPostRequest.from_json(json)
# print the JSON string representation of the object
print CsvUploadsPostRequest.to_json()

# convert the object into a dict
csv_uploads_post_request_dict = csv_uploads_post_request_instance.to_dict()
# create an instance of CsvUploadsPostRequest from a dict
csv_uploads_post_request_form_dict = csv_uploads_post_request.from_dict(csv_uploads_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


