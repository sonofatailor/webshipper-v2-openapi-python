# OrderChannelAccessesIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrderChannelAccessesIdGet200ResponseData**](OrderChannelAccessesIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**OrderChannelAccessesIdGet200ResponseRelationships**](OrderChannelAccessesIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[OrderChannelAccessesIdGet200ResponseIncludedInner]**](OrderChannelAccessesIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_channel_accesses_id_get200_response import OrderChannelAccessesIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelAccessesIdGet200Response from a JSON string
order_channel_accesses_id_get200_response_instance = OrderChannelAccessesIdGet200Response.from_json(json)
# print the JSON string representation of the object
print OrderChannelAccessesIdGet200Response.to_json()

# convert the object into a dict
order_channel_accesses_id_get200_response_dict = order_channel_accesses_id_get200_response_instance.to_dict()
# create an instance of OrderChannelAccessesIdGet200Response from a dict
order_channel_accesses_id_get200_response_form_dict = order_channel_accesses_id_get200_response.from_dict(order_channel_accesses_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


