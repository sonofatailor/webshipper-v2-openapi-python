# ShippingAddressesGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ShippingAddressesGet200ResponseDataInner]**](ShippingAddressesGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.shipping_addresses_get200_response import ShippingAddressesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingAddressesGet200Response from a JSON string
shipping_addresses_get200_response_instance = ShippingAddressesGet200Response.from_json(json)
# print the JSON string representation of the object
print ShippingAddressesGet200Response.to_json()

# convert the object into a dict
shipping_addresses_get200_response_dict = shipping_addresses_get200_response_instance.to_dict()
# create an instance of ShippingAddressesGet200Response from a dict
shipping_addresses_get200_response_form_dict = shipping_addresses_get200_response.from_dict(shipping_addresses_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


