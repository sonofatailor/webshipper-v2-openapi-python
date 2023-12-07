# ShippingRatesIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ShippingRatesIdGet200ResponseData**](ShippingRatesIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**ShippingRatesIdGet200ResponseRelationships**](ShippingRatesIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[ShippingRatesIdGet200ResponseIncludedInner]**](ShippingRatesIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.shipping_rates_id_get200_response import ShippingRatesIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingRatesIdGet200Response from a JSON string
shipping_rates_id_get200_response_instance = ShippingRatesIdGet200Response.from_json(json)
# print the JSON string representation of the object
print ShippingRatesIdGet200Response.to_json()

# convert the object into a dict
shipping_rates_id_get200_response_dict = shipping_rates_id_get200_response_instance.to_dict()
# create an instance of ShippingRatesIdGet200Response from a dict
shipping_rates_id_get200_response_form_dict = shipping_rates_id_get200_response.from_dict(shipping_rates_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


