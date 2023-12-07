# PrinterClientsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PrinterClientsIdGet200ResponseData**](PrinterClientsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**PrinterClientsIdGet200ResponseRelationships**](PrinterClientsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.printer_clients_id_patch_request import PrinterClientsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterClientsIdPatchRequest from a JSON string
printer_clients_id_patch_request_instance = PrinterClientsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print PrinterClientsIdPatchRequest.to_json()

# convert the object into a dict
printer_clients_id_patch_request_dict = printer_clients_id_patch_request_instance.to_dict()
# create an instance of PrinterClientsIdPatchRequest from a dict
printer_clients_id_patch_request_form_dict = printer_clients_id_patch_request.from_dict(printer_clients_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


