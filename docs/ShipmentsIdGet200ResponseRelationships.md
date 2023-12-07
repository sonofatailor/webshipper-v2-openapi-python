# ShipmentsIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | [**BarcodeRangesIdGet200ResponseRelationshipsCarrier**](BarcodeRangesIdGet200ResponseRelationshipsCarrier.md) |  | [optional] 
**order** | [**AdditionalAttributesIdGet200ResponseRelationshipsOrder**](AdditionalAttributesIdGet200ResponseRelationshipsOrder.md) |  | [optional] 
**shipping_rate** | [**OrdersIdGet200ResponseRelationshipsShippingRate**](OrdersIdGet200ResponseRelationshipsShippingRate.md) |  | [optional] 
**printer_client** | [**OrdersIdGet200ResponseRelationshipsPrinterClient**](OrdersIdGet200ResponseRelationshipsPrinterClient.md) |  | [optional] 
**original_shipment** | [**EdisIdGet200ResponseRelationshipsShipment**](EdisIdGet200ResponseRelationshipsShipment.md) |  | [optional] 
**pickup** | [**ShipmentsIdGet200ResponseRelationshipsPickup**](ShipmentsIdGet200ResponseRelationshipsPickup.md) |  | [optional] 
**shadow_shipment** | [**EdisIdGet200ResponseRelationshipsShipment**](EdisIdGet200ResponseRelationshipsShipment.md) |  | [optional] 
**var_return** | [**ShipmentsIdGet200ResponseRelationshipsReturn**](ShipmentsIdGet200ResponseRelationshipsReturn.md) |  | [optional] 
**document_template** | [**ShipmentsIdGet200ResponseRelationshipsDocumentTemplate**](ShipmentsIdGet200ResponseRelationshipsDocumentTemplate.md) |  | [optional] 
**mail_template** | [**ReturnPortalsIdGet200ResponseRelationshipsMailTemplate**](ReturnPortalsIdGet200ResponseRelationshipsMailTemplate.md) |  | [optional] 
**return_label_mail_template** | [**ReturnPortalsIdGet200ResponseRelationshipsMailTemplate**](ReturnPortalsIdGet200ResponseRelationshipsMailTemplate.md) |  | [optional] 

## Example

```python
from webshipperv2.models.shipments_id_get200_response_relationships import ShipmentsIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentsIdGet200ResponseRelationships from a JSON string
shipments_id_get200_response_relationships_instance = ShipmentsIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print ShipmentsIdGet200ResponseRelationships.to_json()

# convert the object into a dict
shipments_id_get200_response_relationships_dict = shipments_id_get200_response_relationships_instance.to_dict()
# create an instance of ShipmentsIdGet200ResponseRelationships from a dict
shipments_id_get200_response_relationships_form_dict = shipments_id_get200_response_relationships.from_dict(shipments_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


