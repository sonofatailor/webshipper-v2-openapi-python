# OrderChannelAccessesIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_channel** | [**CsvMappingsIdGet200ResponseRelationshipsOrderChannel**](CsvMappingsIdGet200ResponseRelationshipsOrderChannel.md) |  | [optional] 
**user** | [**CarrierAccessesIdGet200ResponseRelationshipsUser**](CarrierAccessesIdGet200ResponseRelationshipsUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_channel_accesses_id_get200_response_relationships import OrderChannelAccessesIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelAccessesIdGet200ResponseRelationships from a JSON string
order_channel_accesses_id_get200_response_relationships_instance = OrderChannelAccessesIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print OrderChannelAccessesIdGet200ResponseRelationships.to_json()

# convert the object into a dict
order_channel_accesses_id_get200_response_relationships_dict = order_channel_accesses_id_get200_response_relationships_instance.to_dict()
# create an instance of OrderChannelAccessesIdGet200ResponseRelationships from a dict
order_channel_accesses_id_get200_response_relationships_form_dict = order_channel_accesses_id_get200_response_relationships.from_dict(order_channel_accesses_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


