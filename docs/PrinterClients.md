# PrinterClients


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique ID of the printer client | [optional] 
**approved** | **bool** | DEPRECATED | [optional] 
**alias** | **str** | Defaults to the host name of the machine running the client  | [optional] 
**is_online** | **bool** | Shows if the printer client is online | [optional] 
**last_connected** | **str** | Shows when the printer client was last connected | [optional] 
**prevent_multiple_shipments** | **bool** |  | [optional] 

## Example

```python
from webshipperv2.models.printer_clients import PrinterClients

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterClients from a JSON string
printer_clients_instance = PrinterClients.from_json(json)
# print the JSON string representation of the object
print PrinterClients.to_json()

# convert the object into a dict
printer_clients_dict = printer_clients_instance.to_dict()
# create an instance of PrinterClients from a dict
printer_clients_form_dict = printer_clients.from_dict(printer_clients_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


