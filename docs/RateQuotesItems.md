# RateQuotesItems


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **str** | Price in some currency | [optional] [readonly] 

## Example

```python
from openapi_client.models.rate_quotes_items import RateQuotesItems

# TODO update the JSON string below
json = "{}"
# create an instance of RateQuotesItems from a JSON string
rate_quotes_items_instance = RateQuotesItems.from_json(json)
# print the JSON string representation of the object
print RateQuotesItems.to_json()

# convert the object into a dict
rate_quotes_items_dict = rate_quotes_items_instance.to_dict()
# create an instance of RateQuotesItems from a dict
rate_quotes_items_form_dict = rate_quotes_items.from_dict(rate_quotes_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


