# PrinterClientsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PrinterClientsGet200ResponseDataInner]**](PrinterClientsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.printer_clients_get200_response import PrinterClientsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterClientsGet200Response from a JSON string
printer_clients_get200_response_instance = PrinterClientsGet200Response.from_json(json)
# print the JSON string representation of the object
print PrinterClientsGet200Response.to_json()

# convert the object into a dict
printer_clients_get200_response_dict = printer_clients_get200_response_instance.to_dict()
# create an instance of PrinterClientsGet200Response from a dict
printer_clients_get200_response_form_dict = printer_clients_get200_response.from_dict(printer_clients_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


