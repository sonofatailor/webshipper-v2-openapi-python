# WaybillsIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | [**BarcodeRangesIdGet200ResponseRelationshipsCarrier**](BarcodeRangesIdGet200ResponseRelationshipsCarrier.md) |  | [optional] 
**sold_to_address** | [**CarriersIdGet200ResponseRelationshipsSenderAddress**](CarriersIdGet200ResponseRelationshipsSenderAddress.md) |  | [optional] 
**sender_address** | [**CarriersIdGet200ResponseRelationshipsSenderAddress**](CarriersIdGet200ResponseRelationshipsSenderAddress.md) |  | [optional] 
**document_template** | [**ShipmentsIdGet200ResponseRelationshipsDocumentTemplate**](ShipmentsIdGet200ResponseRelationshipsDocumentTemplate.md) |  | [optional] 
**printer_client** | [**OrdersIdGet200ResponseRelationshipsPrinterClient**](OrdersIdGet200ResponseRelationshipsPrinterClient.md) |  | [optional] 

## Example

```python
from webshipperv2.models.waybills_id_get200_response_relationships import WaybillsIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of WaybillsIdGet200ResponseRelationships from a JSON string
waybills_id_get200_response_relationships_instance = WaybillsIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print WaybillsIdGet200ResponseRelationships.to_json()

# convert the object into a dict
waybills_id_get200_response_relationships_dict = waybills_id_get200_response_relationships_instance.to_dict()
# create an instance of WaybillsIdGet200ResponseRelationships from a dict
waybills_id_get200_response_relationships_form_dict = waybills_id_get200_response_relationships.from_dict(waybills_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


