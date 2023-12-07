# ReportsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReportsPostRequestData**](ReportsPostRequestData.md) |  | [optional] 
**relationships** | [**ReportsIdGet200ResponseRelationships**](ReportsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.reports_post_request import ReportsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportsPostRequest from a JSON string
reports_post_request_instance = ReportsPostRequest.from_json(json)
# print the JSON string representation of the object
print ReportsPostRequest.to_json()

# convert the object into a dict
reports_post_request_dict = reports_post_request_instance.to_dict()
# create an instance of ReportsPostRequest from a dict
reports_post_request_form_dict = reports_post_request.from_dict(reports_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


