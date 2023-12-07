# OrderChannelAccessesIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrderChannelAccessesIdGet200ResponseData**](OrderChannelAccessesIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**OrderChannelAccessesIdGet200ResponseRelationships**](OrderChannelAccessesIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_channel_accesses_id_patch_request import OrderChannelAccessesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelAccessesIdPatchRequest from a JSON string
order_channel_accesses_id_patch_request_instance = OrderChannelAccessesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print OrderChannelAccessesIdPatchRequest.to_json()

# convert the object into a dict
order_channel_accesses_id_patch_request_dict = order_channel_accesses_id_patch_request_instance.to_dict()
# create an instance of OrderChannelAccessesIdPatchRequest from a dict
order_channel_accesses_id_patch_request_form_dict = order_channel_accesses_id_patch_request.from_dict(order_channel_accesses_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


