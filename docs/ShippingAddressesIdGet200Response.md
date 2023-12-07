# ShippingAddressesIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ShippingAddressesIdGet200ResponseData**](ShippingAddressesIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipping_addresses_id_get200_response import ShippingAddressesIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingAddressesIdGet200Response from a JSON string
shipping_addresses_id_get200_response_instance = ShippingAddressesIdGet200Response.from_json(json)
# print the JSON string representation of the object
print ShippingAddressesIdGet200Response.to_json()

# convert the object into a dict
shipping_addresses_id_get200_response_dict = shipping_addresses_id_get200_response_instance.to_dict()
# create an instance of ShippingAddressesIdGet200Response from a dict
shipping_addresses_id_get200_response_form_dict = shipping_addresses_id_get200_response.from_dict(shipping_addresses_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


