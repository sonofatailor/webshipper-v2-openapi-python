# OrderChannelTypes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**support_url** | **str** |  | [optional] 
**public_global_attrs** | **str** |  | [optional] 
**list_logo** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**module_link** | **str** |  | [optional] 
**can_autofulfill** | **bool** |  | [optional] 
**can_limit_drop_points** | **bool** |  | [optional] 
**supports_rate_quoting** | **bool** |  | [optional] 
**uses_scheduled_import** | **bool** |  | [optional] 
**supports_time_interval_import** | **bool** |  | [optional] 
**supports_statuses_import** | **bool** |  | [optional] 
**supports_id_import** | **bool** |  | [optional] 
**supports_vat_in_checkout** | **bool** |  | [optional] 

## Example

```python
from webshipperv2.models.order_channel_types import OrderChannelTypes

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelTypes from a JSON string
order_channel_types_instance = OrderChannelTypes.from_json(json)
# print the JSON string representation of the object
print OrderChannelTypes.to_json()

# convert the object into a dict
order_channel_types_dict = order_channel_types_instance.to_dict()
# create an instance of OrderChannelTypes from a dict
order_channel_types_form_dict = order_channel_types.from_dict(order_channel_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


