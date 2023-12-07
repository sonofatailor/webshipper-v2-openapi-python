# RateQuotesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RateQuotesPostRequestData**](RateQuotesPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.rate_quotes_post_request import RateQuotesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RateQuotesPostRequest from a JSON string
rate_quotes_post_request_instance = RateQuotesPostRequest.from_json(json)
# print the JSON string representation of the object
print RateQuotesPostRequest.to_json()

# convert the object into a dict
rate_quotes_post_request_dict = rate_quotes_post_request_instance.to_dict()
# create an instance of RateQuotesPostRequest from a dict
rate_quotes_post_request_form_dict = rate_quotes_post_request.from_dict(rate_quotes_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


