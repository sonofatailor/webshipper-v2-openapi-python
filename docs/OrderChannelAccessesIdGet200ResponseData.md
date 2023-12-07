# OrderChannelAccessesIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**OrderChannelAccesses**](OrderChannelAccesses.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_channel_accesses_id_get200_response_data import OrderChannelAccessesIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelAccessesIdGet200ResponseData from a JSON string
order_channel_accesses_id_get200_response_data_instance = OrderChannelAccessesIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print OrderChannelAccessesIdGet200ResponseData.to_json()

# convert the object into a dict
order_channel_accesses_id_get200_response_data_dict = order_channel_accesses_id_get200_response_data_instance.to_dict()
# create an instance of OrderChannelAccessesIdGet200ResponseData from a dict
order_channel_accesses_id_get200_response_data_form_dict = order_channel_accesses_id_get200_response_data.from_dict(order_channel_accesses_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


