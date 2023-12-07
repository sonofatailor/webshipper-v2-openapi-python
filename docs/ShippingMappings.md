# ShippingMappings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_code** | **str** | Shipping code is a unique identifier from the order channel that will be mapped to a shipping rate | [optional] 
**shipping_name** | **str** | Shipping name is a human readable identifier of the shipping method | [optional] 
**shipping_rate_id** | **int** | Shipping rate id is the id of the shipping rate which you want to map to. | [optional] 
**order_channel_id** | **int** | Order channel id of the order channel | [optional] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 

## Example

```python
from webshipperv2.models.shipping_mappings import ShippingMappings

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingMappings from a JSON string
shipping_mappings_instance = ShippingMappings.from_json(json)
# print the JSON string representation of the object
print ShippingMappings.to_json()

# convert the object into a dict
shipping_mappings_dict = shipping_mappings_instance.to_dict()
# create an instance of ShippingMappings from a dict
shipping_mappings_form_dict = shipping_mappings.from_dict(shipping_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


