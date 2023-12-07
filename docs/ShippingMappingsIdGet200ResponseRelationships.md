# ShippingMappingsIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_rate** | [**OrdersIdGet200ResponseRelationshipsShippingRate**](OrdersIdGet200ResponseRelationshipsShippingRate.md) |  | [optional] 
**order_channel** | [**CsvMappingsIdGet200ResponseRelationshipsOrderChannel**](CsvMappingsIdGet200ResponseRelationshipsOrderChannel.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipping_mappings_id_get200_response_relationships import ShippingMappingsIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingMappingsIdGet200ResponseRelationships from a JSON string
shipping_mappings_id_get200_response_relationships_instance = ShippingMappingsIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print ShippingMappingsIdGet200ResponseRelationships.to_json()

# convert the object into a dict
shipping_mappings_id_get200_response_relationships_dict = shipping_mappings_id_get200_response_relationships_instance.to_dict()
# create an instance of ShippingMappingsIdGet200ResponseRelationships from a dict
shipping_mappings_id_get200_response_relationships_form_dict = shipping_mappings_id_get200_response_relationships.from_dict(shipping_mappings_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


