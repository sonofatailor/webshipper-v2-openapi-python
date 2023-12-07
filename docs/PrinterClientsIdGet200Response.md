# PrinterClientsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PrinterClientsIdGet200ResponseData**](PrinterClientsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**PrinterClientsIdGet200ResponseRelationships**](PrinterClientsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[PrinterClientsIdGet200ResponseIncludedInner]**](PrinterClientsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.printer_clients_id_get200_response import PrinterClientsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterClientsIdGet200Response from a JSON string
printer_clients_id_get200_response_instance = PrinterClientsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print PrinterClientsIdGet200Response.to_json()

# convert the object into a dict
printer_clients_id_get200_response_dict = printer_clients_id_get200_response_instance.to_dict()
# create an instance of PrinterClientsIdGet200Response from a dict
printer_clients_id_get200_response_form_dict = printer_clients_id_get200_response.from_dict(printer_clients_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


