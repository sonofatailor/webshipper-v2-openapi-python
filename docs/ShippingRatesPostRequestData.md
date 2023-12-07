# ShippingRatesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**ShippingRates**](ShippingRates.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipping_rates_post_request_data import ShippingRatesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingRatesPostRequestData from a JSON string
shipping_rates_post_request_data_instance = ShippingRatesPostRequestData.from_json(json)
# print the JSON string representation of the object
print ShippingRatesPostRequestData.to_json()

# convert the object into a dict
shipping_rates_post_request_data_dict = shipping_rates_post_request_data_instance.to_dict()
# create an instance of ShippingRatesPostRequestData from a dict
shipping_rates_post_request_data_form_dict = shipping_rates_post_request_data.from_dict(shipping_rates_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


