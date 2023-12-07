# ShippingMappingsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ShippingMappingsPostRequestData**](ShippingMappingsPostRequestData.md) |  | [optional] 
**relationships** | [**ShippingMappingsIdGet200ResponseRelationships**](ShippingMappingsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.shipping_mappings_post_request import ShippingMappingsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingMappingsPostRequest from a JSON string
shipping_mappings_post_request_instance = ShippingMappingsPostRequest.from_json(json)
# print the JSON string representation of the object
print ShippingMappingsPostRequest.to_json()

# convert the object into a dict
shipping_mappings_post_request_dict = shipping_mappings_post_request_instance.to_dict()
# create an instance of ShippingMappingsPostRequest from a dict
shipping_mappings_post_request_form_dict = shipping_mappings_post_request.from_dict(shipping_mappings_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


