# ServiceQuotesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceQuotesPostRequestData**](ServiceQuotesPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.service_quotes_post_request import ServiceQuotesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQuotesPostRequest from a JSON string
service_quotes_post_request_instance = ServiceQuotesPostRequest.from_json(json)
# print the JSON string representation of the object
print ServiceQuotesPostRequest.to_json()

# convert the object into a dict
service_quotes_post_request_dict = service_quotes_post_request_instance.to_dict()
# create an instance of ServiceQuotesPostRequest from a dict
service_quotes_post_request_form_dict = service_quotes_post_request.from_dict(service_quotes_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


