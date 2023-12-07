# ShippingAddressesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**ShippingAddresses**](ShippingAddresses.md) |  | [optional] 

## Example

```python
from webshipperv2.models.shipping_addresses_post_request_data import ShippingAddressesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingAddressesPostRequestData from a JSON string
shipping_addresses_post_request_data_instance = ShippingAddressesPostRequestData.from_json(json)
# print the JSON string representation of the object
print ShippingAddressesPostRequestData.to_json()

# convert the object into a dict
shipping_addresses_post_request_data_dict = shipping_addresses_post_request_data_instance.to_dict()
# create an instance of ShippingAddressesPostRequestData from a dict
shipping_addresses_post_request_data_form_dict = shipping_addresses_post_request_data.from_dict(shipping_addresses_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


