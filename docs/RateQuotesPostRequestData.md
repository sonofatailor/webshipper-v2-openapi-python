# RateQuotesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**RateQuotes**](RateQuotes.md) |  | [optional] 

## Example

```python
from openapi_client.models.rate_quotes_post_request_data import RateQuotesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of RateQuotesPostRequestData from a JSON string
rate_quotes_post_request_data_instance = RateQuotesPostRequestData.from_json(json)
# print the JSON string representation of the object
print RateQuotesPostRequestData.to_json()

# convert the object into a dict
rate_quotes_post_request_data_dict = rate_quotes_post_request_data_instance.to_dict()
# create an instance of RateQuotesPostRequestData from a dict
rate_quotes_post_request_data_form_dict = rate_quotes_post_request_data.from_dict(rate_quotes_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


