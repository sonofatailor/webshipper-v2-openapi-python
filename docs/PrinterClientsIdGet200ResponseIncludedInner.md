# PrinterClientsIdGet200ResponseIncludedInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**data** | [**PrinterClientsIdGet200ResponseIncludedInnerData**](PrinterClientsIdGet200ResponseIncludedInnerData.md) |  | [optional] 

## Example

```python
from openapi_client.models.printer_clients_id_get200_response_included_inner import PrinterClientsIdGet200ResponseIncludedInner

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterClientsIdGet200ResponseIncludedInner from a JSON string
printer_clients_id_get200_response_included_inner_instance = PrinterClientsIdGet200ResponseIncludedInner.from_json(json)
# print the JSON string representation of the object
print PrinterClientsIdGet200ResponseIncludedInner.to_json()

# convert the object into a dict
printer_clients_id_get200_response_included_inner_dict = printer_clients_id_get200_response_included_inner_instance.to_dict()
# create an instance of PrinterClientsIdGet200ResponseIncludedInner from a dict
printer_clients_id_get200_response_included_inner_form_dict = printer_clients_id_get200_response_included_inner.from_dict(printer_clients_id_get200_response_included_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


