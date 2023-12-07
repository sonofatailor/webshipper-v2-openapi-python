# ShippingRatesIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | [**BarcodeRangesIdGet200ResponseRelationshipsCarrier**](BarcodeRangesIdGet200ResponseRelationshipsCarrier.md) |  | [optional] 
**order_channel** | [**CsvMappingsIdGet200ResponseRelationshipsOrderChannel**](CsvMappingsIdGet200ResponseRelationshipsOrderChannel.md) |  | [optional] 
**return_shipping_rate** | [**OrdersIdGet200ResponseRelationshipsShippingRate**](OrdersIdGet200ResponseRelationshipsShippingRate.md) |  | [optional] 
**sender_address** | [**CarriersIdGet200ResponseRelationshipsSenderAddress**](CarriersIdGet200ResponseRelationshipsSenderAddress.md) |  | [optional] 
**return_address** | [**CarriersIdGet200ResponseRelationshipsSenderAddress**](CarriersIdGet200ResponseRelationshipsSenderAddress.md) |  | [optional] 
**mail_template** | [**ReturnPortalsIdGet200ResponseRelationshipsMailTemplate**](ReturnPortalsIdGet200ResponseRelationshipsMailTemplate.md) |  | [optional] 
**return_mail_template** | [**ReturnPortalsIdGet200ResponseRelationshipsMailTemplate**](ReturnPortalsIdGet200ResponseRelationshipsMailTemplate.md) |  | [optional] 
**document_template** | [**ShipmentsIdGet200ResponseRelationshipsDocumentTemplate**](ShipmentsIdGet200ResponseRelationshipsDocumentTemplate.md) |  | [optional] 
**shadow_booking_shipping_rate** | [**OrdersIdGet200ResponseRelationshipsShippingRate**](OrdersIdGet200ResponseRelationshipsShippingRate.md) |  | [optional] 

## Example

```python
from webshipperv2.models.shipping_rates_id_get200_response_relationships import ShippingRatesIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingRatesIdGet200ResponseRelationships from a JSON string
shipping_rates_id_get200_response_relationships_instance = ShippingRatesIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print ShippingRatesIdGet200ResponseRelationships.to_json()

# convert the object into a dict
shipping_rates_id_get200_response_relationships_dict = shipping_rates_id_get200_response_relationships_instance.to_dict()
# create an instance of ShippingRatesIdGet200ResponseRelationships from a dict
shipping_rates_id_get200_response_relationships_form_dict = shipping_rates_id_get200_response_relationships.from_dict(shipping_rates_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


