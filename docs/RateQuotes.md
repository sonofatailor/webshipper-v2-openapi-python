# RateQuotes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quotes** | [**List[RateQuotesItems]**](RateQuotesItems.md) | Array of quotes | [optional] [readonly] 
**success** | **str** | DEPRECATED. The request will return an error response if the quote failed. | [optional] [readonly] 
**delivery_address** | **object** | Delivery address for the quote. Flattened resource of &#39;Shipping Address&#39; | [optional] 
**price** | **int** | The total price of the items | [optional] 
**weight** | **float** | Weight for the quote. | [optional] 
**weight_unit** | **str** | The weight unit. Possible values: g, kg, lbs, oz. | [optional] 
**height** | **float** | Height for the quote. The unit must match the unit you are using for shipping rate configurations. | [optional] 
**length** | **float** | Length for the quote. The unit must match the unit you are using for shipping rate configurations. | [optional] 
**width** | **float** | Width for the quote. The unit must match the unit you are using for shipping rate configurations. | [optional] 
**dimensions_unit** | **str** | Dimensions unit. Possible values: cm, m, in, ft | [optional] 
**sender_address** | **object** | Delivery address for the quote. Flattened resource of &#39;Shipping Address&#39; | [optional] 
**items** | [**List[RateQuotesItems1Inner]**](RateQuotesItems1Inner.md) | Array of items, each item should have fields &lt;code&gt;quantity&lt;/code&gt;, &lt;code&gt;sku&lt;/code&gt;, &lt;code&gt;description&lt;/code&gt; | [optional] 
**order_channel_id** | **int** | The id of the order channel for which to get shipping rates. | [optional] 
**currency** | **str** |  | [optional] 
**include_hidden** | **bool** | Also include shipping rates which are normally hidden during checkout. | [optional] 
**is_return** | **bool** | Set to true to quote for return rates. If false standard rates are quoted. Default: false. | [optional] 
**additional_attributes** | **str** | Possibility to add hash of additional attributes for filtering. | [optional] 
**filter_by_currency** | **str** |  | [optional] 

## Example

```python
from webshipperv2.models.rate_quotes import RateQuotes

# TODO update the JSON string below
json = "{}"
# create an instance of RateQuotes from a JSON string
rate_quotes_instance = RateQuotes.from_json(json)
# print the JSON string representation of the object
print RateQuotes.to_json()

# convert the object into a dict
rate_quotes_dict = rate_quotes_instance.to_dict()
# create an instance of RateQuotes from a dict
rate_quotes_form_dict = rate_quotes.from_dict(rate_quotes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


