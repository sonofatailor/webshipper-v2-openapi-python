# ShippingMappingsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ShippingMappingsGet200ResponseDataInner]**](ShippingMappingsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipping_mappings_get200_response import ShippingMappingsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingMappingsGet200Response from a JSON string
shipping_mappings_get200_response_instance = ShippingMappingsGet200Response.from_json(json)
# print the JSON string representation of the object
print ShippingMappingsGet200Response.to_json()

# convert the object into a dict
shipping_mappings_get200_response_dict = shipping_mappings_get200_response_instance.to_dict()
# create an instance of ShippingMappingsGet200Response from a dict
shipping_mappings_get200_response_form_dict = shipping_mappings_get200_response.from_dict(shipping_mappings_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


