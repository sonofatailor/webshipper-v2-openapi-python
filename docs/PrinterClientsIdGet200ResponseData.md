# PrinterClientsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**PrinterClients**](PrinterClients.md) |  | [optional] 

## Example

```python
from openapi_client.models.printer_clients_id_get200_response_data import PrinterClientsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterClientsIdGet200ResponseData from a JSON string
printer_clients_id_get200_response_data_instance = PrinterClientsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print PrinterClientsIdGet200ResponseData.to_json()

# convert the object into a dict
printer_clients_id_get200_response_data_dict = printer_clients_id_get200_response_data_instance.to_dict()
# create an instance of PrinterClientsIdGet200ResponseData from a dict
printer_clients_id_get200_response_data_form_dict = printer_clients_id_get200_response_data.from_dict(printer_clients_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


