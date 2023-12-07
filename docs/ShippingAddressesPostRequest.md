# ShippingAddressesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ShippingAddressesPostRequestData**](ShippingAddressesPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.shipping_addresses_post_request import ShippingAddressesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingAddressesPostRequest from a JSON string
shipping_addresses_post_request_instance = ShippingAddressesPostRequest.from_json(json)
# print the JSON string representation of the object
print ShippingAddressesPostRequest.to_json()

# convert the object into a dict
shipping_addresses_post_request_dict = shipping_addresses_post_request_instance.to_dict()
# create an instance of ShippingAddressesPostRequest from a dict
shipping_addresses_post_request_form_dict = shipping_addresses_post_request.from_dict(shipping_addresses_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


