# OrderChannelAccesses


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 

## Example

```python
from openapi_client.models.order_channel_accesses import OrderChannelAccesses

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelAccesses from a JSON string
order_channel_accesses_instance = OrderChannelAccesses.from_json(json)
# print the JSON string representation of the object
print OrderChannelAccesses.to_json()

# convert the object into a dict
order_channel_accesses_dict = order_channel_accesses_instance.to_dict()
# create an instance of OrderChannelAccesses from a dict
order_channel_accesses_form_dict = order_channel_accesses.from_dict(order_channel_accesses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


