# ShippingMappingsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ShippingMappingsIdGet200ResponseData**](ShippingMappingsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**ShippingMappingsIdGet200ResponseRelationships**](ShippingMappingsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.shipping_mappings_id_patch_request import ShippingMappingsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingMappingsIdPatchRequest from a JSON string
shipping_mappings_id_patch_request_instance = ShippingMappingsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ShippingMappingsIdPatchRequest.to_json()

# convert the object into a dict
shipping_mappings_id_patch_request_dict = shipping_mappings_id_patch_request_instance.to_dict()
# create an instance of ShippingMappingsIdPatchRequest from a dict
shipping_mappings_id_patch_request_form_dict = shipping_mappings_id_patch_request.from_dict(shipping_mappings_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


