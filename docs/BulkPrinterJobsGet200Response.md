# BulkPrinterJobsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BulkPrinterJobsGet200ResponseDataInner]**](BulkPrinterJobsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.bulk_printer_jobs_get200_response import BulkPrinterJobsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPrinterJobsGet200Response from a JSON string
bulk_printer_jobs_get200_response_instance = BulkPrinterJobsGet200Response.from_json(json)
# print the JSON string representation of the object
print BulkPrinterJobsGet200Response.to_json()

# convert the object into a dict
bulk_printer_jobs_get200_response_dict = bulk_printer_jobs_get200_response_instance.to_dict()
# create an instance of BulkPrinterJobsGet200Response from a dict
bulk_printer_jobs_get200_response_form_dict = bulk_printer_jobs_get200_response.from_dict(bulk_printer_jobs_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


