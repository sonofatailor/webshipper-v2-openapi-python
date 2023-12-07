# RateQuotesPost204Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RateQuotesPost204ResponseData**](RateQuotesPost204ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.rate_quotes_post204_response import RateQuotesPost204Response

# TODO update the JSON string below
json = "{}"
# create an instance of RateQuotesPost204Response from a JSON string
rate_quotes_post204_response_instance = RateQuotesPost204Response.from_json(json)
# print the JSON string representation of the object
print RateQuotesPost204Response.to_json()

# convert the object into a dict
rate_quotes_post204_response_dict = rate_quotes_post204_response_instance.to_dict()
# create an instance of RateQuotesPost204Response from a dict
rate_quotes_post204_response_form_dict = rate_quotes_post204_response.from_dict(rate_quotes_post204_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


