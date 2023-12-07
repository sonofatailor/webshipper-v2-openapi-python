# PrinterClientsIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_printer** | [**PrinterClientsIdGet200ResponseRelationshipsLabelPrinter**](PrinterClientsIdGet200ResponseRelationshipsLabelPrinter.md) |  | [optional] 
**zpl_printer** | [**PrinterClientsIdGet200ResponseRelationshipsLabelPrinter**](PrinterClientsIdGet200ResponseRelationshipsLabelPrinter.md) |  | [optional] 
**document_printer** | [**PrinterClientsIdGet200ResponseRelationshipsLabelPrinter**](PrinterClientsIdGet200ResponseRelationshipsLabelPrinter.md) |  | [optional] 
**location** | [**CarriersIdGet200ResponseRelationshipsSenderAddress**](CarriersIdGet200ResponseRelationshipsSenderAddress.md) |  | [optional] 

## Example

```python
from webshipperv2.models.printer_clients_id_get200_response_relationships import PrinterClientsIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterClientsIdGet200ResponseRelationships from a JSON string
printer_clients_id_get200_response_relationships_instance = PrinterClientsIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print PrinterClientsIdGet200ResponseRelationships.to_json()

# convert the object into a dict
printer_clients_id_get200_response_relationships_dict = printer_clients_id_get200_response_relationships_instance.to_dict()
# create an instance of PrinterClientsIdGet200ResponseRelationships from a dict
printer_clients_id_get200_response_relationships_form_dict = printer_clients_id_get200_response_relationships.from_dict(printer_clients_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


