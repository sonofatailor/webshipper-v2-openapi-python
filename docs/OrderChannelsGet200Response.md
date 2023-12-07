# OrderChannelsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OrderChannelsGet200ResponseDataInner]**](OrderChannelsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.order_channels_get200_response import OrderChannelsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelsGet200Response from a JSON string
order_channels_get200_response_instance = OrderChannelsGet200Response.from_json(json)
# print the JSON string representation of the object
print OrderChannelsGet200Response.to_json()

# convert the object into a dict
order_channels_get200_response_dict = order_channels_get200_response_instance.to_dict()
# create an instance of OrderChannelsGet200Response from a dict
order_channels_get200_response_form_dict = order_channels_get200_response.from_dict(order_channels_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


