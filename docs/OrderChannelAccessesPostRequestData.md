# OrderChannelAccessesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**OrderChannelAccesses**](OrderChannelAccesses.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_channel_accesses_post_request_data import OrderChannelAccessesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelAccessesPostRequestData from a JSON string
order_channel_accesses_post_request_data_instance = OrderChannelAccessesPostRequestData.from_json(json)
# print the JSON string representation of the object
print OrderChannelAccessesPostRequestData.to_json()

# convert the object into a dict
order_channel_accesses_post_request_data_dict = order_channel_accesses_post_request_data_instance.to_dict()
# create an instance of OrderChannelAccessesPostRequestData from a dict
order_channel_accesses_post_request_data_form_dict = order_channel_accesses_post_request_data.from_dict(order_channel_accesses_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


