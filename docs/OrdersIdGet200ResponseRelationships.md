# OrdersIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_channel** | [**CsvMappingsIdGet200ResponseRelationshipsOrderChannel**](CsvMappingsIdGet200ResponseRelationshipsOrderChannel.md) |  | [optional] 
**shipping_rate** | [**OrdersIdGet200ResponseRelationshipsShippingRate**](OrdersIdGet200ResponseRelationshipsShippingRate.md) |  | [optional] 
**error_type** | [**OrdersIdGet200ResponseRelationshipsErrorType**](OrdersIdGet200ResponseRelationshipsErrorType.md) |  | [optional] 
**printer_client** | [**OrdersIdGet200ResponseRelationshipsPrinterClient**](OrdersIdGet200ResponseRelationshipsPrinterClient.md) |  | [optional] 

## Example

```python
from openapi_client.models.orders_id_get200_response_relationships import OrdersIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersIdGet200ResponseRelationships from a JSON string
orders_id_get200_response_relationships_instance = OrdersIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print OrdersIdGet200ResponseRelationships.to_json()

# convert the object into a dict
orders_id_get200_response_relationships_dict = orders_id_get200_response_relationships_instance.to_dict()
# create an instance of OrdersIdGet200ResponseRelationships from a dict
orders_id_get200_response_relationships_form_dict = orders_id_get200_response_relationships.from_dict(orders_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


