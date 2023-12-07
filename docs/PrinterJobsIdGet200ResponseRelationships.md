# PrinterJobsIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**printer_client** | [**OrdersIdGet200ResponseRelationshipsPrinterClient**](OrdersIdGet200ResponseRelationshipsPrinterClient.md) |  | [optional] 
**printer** | [**PrinterClientsIdGet200ResponseRelationshipsLabelPrinter**](PrinterClientsIdGet200ResponseRelationshipsLabelPrinter.md) |  | [optional] 
**printable** | [**PrinterJobsIdGet200ResponseRelationshipsPrintable**](PrinterJobsIdGet200ResponseRelationshipsPrintable.md) |  | [optional] 

## Example

```python
from webshipperv2.models.printer_jobs_id_get200_response_relationships import PrinterJobsIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterJobsIdGet200ResponseRelationships from a JSON string
printer_jobs_id_get200_response_relationships_instance = PrinterJobsIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print PrinterJobsIdGet200ResponseRelationships.to_json()

# convert the object into a dict
printer_jobs_id_get200_response_relationships_dict = printer_jobs_id_get200_response_relationships_instance.to_dict()
# create an instance of PrinterJobsIdGet200ResponseRelationships from a dict
printer_jobs_id_get200_response_relationships_form_dict = printer_jobs_id_get200_response_relationships.from_dict(printer_jobs_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


