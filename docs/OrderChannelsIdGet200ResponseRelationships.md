# OrderChannelsIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_channel_type** | [**LocalAttrsIdGet200ResponseRelationshipsOrderChannelType**](LocalAttrsIdGet200ResponseRelationshipsOrderChannelType.md) |  | [optional] 
**slip_template** | [**OrderChannelsIdGet200ResponseRelationshipsSlipTemplate**](OrderChannelsIdGet200ResponseRelationshipsSlipTemplate.md) |  | [optional] 
**sender_address** | [**CarriersIdGet200ResponseRelationshipsSenderAddress**](CarriersIdGet200ResponseRelationshipsSenderAddress.md) |  | [optional] 
**return_address** | [**CarriersIdGet200ResponseRelationshipsSenderAddress**](CarriersIdGet200ResponseRelationshipsSenderAddress.md) |  | [optional] 
**pickup_address** | [**CarriersIdGet200ResponseRelationshipsSenderAddress**](CarriersIdGet200ResponseRelationshipsSenderAddress.md) |  | [optional] 
**sold_from_address** | [**CarriersIdGet200ResponseRelationshipsSenderAddress**](CarriersIdGet200ResponseRelationshipsSenderAddress.md) |  | [optional] 
**default_printer_client** | [**OrdersIdGet200ResponseRelationshipsPrinterClient**](OrdersIdGet200ResponseRelationshipsPrinterClient.md) |  | [optional] 

## Example

```python
from webshipperv2.models.order_channels_id_get200_response_relationships import OrderChannelsIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelsIdGet200ResponseRelationships from a JSON string
order_channels_id_get200_response_relationships_instance = OrderChannelsIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print OrderChannelsIdGet200ResponseRelationships.to_json()

# convert the object into a dict
order_channels_id_get200_response_relationships_dict = order_channels_id_get200_response_relationships_instance.to_dict()
# create an instance of OrderChannelsIdGet200ResponseRelationships from a dict
order_channels_id_get200_response_relationships_form_dict = order_channels_id_get200_response_relationships.from_dict(order_channels_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


