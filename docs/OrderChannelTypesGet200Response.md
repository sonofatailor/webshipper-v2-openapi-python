# OrderChannelTypesGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OrderChannelTypesGet200ResponseDataInner]**](OrderChannelTypesGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.order_channel_types_get200_response import OrderChannelTypesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelTypesGet200Response from a JSON string
order_channel_types_get200_response_instance = OrderChannelTypesGet200Response.from_json(json)
# print the JSON string representation of the object
print OrderChannelTypesGet200Response.to_json()

# convert the object into a dict
order_channel_types_get200_response_dict = order_channel_types_get200_response_instance.to_dict()
# create an instance of OrderChannelTypesGet200Response from a dict
order_channel_types_get200_response_form_dict = order_channel_types_get200_response.from_dict(order_channel_types_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


