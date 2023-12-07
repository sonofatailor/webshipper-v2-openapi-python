# BulkPrinterJobsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BulkPrinterJobsIdGet200ResponseData**](BulkPrinterJobsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.bulk_printer_jobs_id_patch_request import BulkPrinterJobsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPrinterJobsIdPatchRequest from a JSON string
bulk_printer_jobs_id_patch_request_instance = BulkPrinterJobsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print BulkPrinterJobsIdPatchRequest.to_json()

# convert the object into a dict
bulk_printer_jobs_id_patch_request_dict = bulk_printer_jobs_id_patch_request_instance.to_dict()
# create an instance of BulkPrinterJobsIdPatchRequest from a dict
bulk_printer_jobs_id_patch_request_form_dict = bulk_printer_jobs_id_patch_request.from_dict(bulk_printer_jobs_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


