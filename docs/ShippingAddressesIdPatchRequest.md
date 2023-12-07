# ShippingAddressesIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ShippingAddressesIdGet200ResponseData**](ShippingAddressesIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.shipping_addresses_id_patch_request import ShippingAddressesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingAddressesIdPatchRequest from a JSON string
shipping_addresses_id_patch_request_instance = ShippingAddressesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ShippingAddressesIdPatchRequest.to_json()

# convert the object into a dict
shipping_addresses_id_patch_request_dict = shipping_addresses_id_patch_request_instance.to_dict()
# create an instance of ShippingAddressesIdPatchRequest from a dict
shipping_addresses_id_patch_request_form_dict = shipping_addresses_id_patch_request.from_dict(shipping_addresses_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


