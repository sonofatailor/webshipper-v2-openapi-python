# OrderChannelAccessesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrderChannelAccessesPostRequestData**](OrderChannelAccessesPostRequestData.md) |  | [optional] 
**relationships** | [**OrderChannelAccessesIdGet200ResponseRelationships**](OrderChannelAccessesIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.order_channel_accesses_post_request import OrderChannelAccessesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelAccessesPostRequest from a JSON string
order_channel_accesses_post_request_instance = OrderChannelAccessesPostRequest.from_json(json)
# print the JSON string representation of the object
print OrderChannelAccessesPostRequest.to_json()

# convert the object into a dict
order_channel_accesses_post_request_dict = order_channel_accesses_post_request_instance.to_dict()
# create an instance of OrderChannelAccessesPostRequest from a dict
order_channel_accesses_post_request_form_dict = order_channel_accesses_post_request.from_dict(order_channel_accesses_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


