# ServiceQuotesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**ServiceQuotes**](ServiceQuotes.md) |  | [optional] 

## Example

```python
from webshipperv2.models.service_quotes_post_request_data import ServiceQuotesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQuotesPostRequestData from a JSON string
service_quotes_post_request_data_instance = ServiceQuotesPostRequestData.from_json(json)
# print the JSON string representation of the object
print ServiceQuotesPostRequestData.to_json()

# convert the object into a dict
service_quotes_post_request_data_dict = service_quotes_post_request_data_instance.to_dict()
# create an instance of ServiceQuotesPostRequestData from a dict
service_quotes_post_request_data_form_dict = service_quotes_post_request_data.from_dict(service_quotes_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


