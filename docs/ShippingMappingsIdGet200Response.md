# ShippingMappingsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ShippingMappingsIdGet200ResponseData**](ShippingMappingsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**ShippingMappingsIdGet200ResponseRelationships**](ShippingMappingsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[ShippingMappingsIdGet200ResponseIncludedInner]**](ShippingMappingsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.shipping_mappings_id_get200_response import ShippingMappingsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingMappingsIdGet200Response from a JSON string
shipping_mappings_id_get200_response_instance = ShippingMappingsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print ShippingMappingsIdGet200Response.to_json()

# convert the object into a dict
shipping_mappings_id_get200_response_dict = shipping_mappings_id_get200_response_instance.to_dict()
# create an instance of ShippingMappingsIdGet200Response from a dict
shipping_mappings_id_get200_response_form_dict = shipping_mappings_id_get200_response.from_dict(shipping_mappings_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


