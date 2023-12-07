# RateQuotesPost204ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**RateQuotes**](RateQuotes.md) |  | [optional] 

## Example

```python
from webshipperv2.models.rate_quotes_post204_response_data import RateQuotesPost204ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RateQuotesPost204ResponseData from a JSON string
rate_quotes_post204_response_data_instance = RateQuotesPost204ResponseData.from_json(json)
# print the JSON string representation of the object
print RateQuotesPost204ResponseData.to_json()

# convert the object into a dict
rate_quotes_post204_response_data_dict = rate_quotes_post204_response_data_instance.to_dict()
# create an instance of RateQuotesPost204ResponseData from a dict
rate_quotes_post204_response_data_form_dict = rate_quotes_post204_response_data.from_dict(rate_quotes_post204_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


