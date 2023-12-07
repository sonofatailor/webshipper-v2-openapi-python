# PrinterRequeueJobsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PrinterRequeueJobsIdGet200ResponseData**](PrinterRequeueJobsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.printer_requeue_jobs_id_patch_request import PrinterRequeueJobsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterRequeueJobsIdPatchRequest from a JSON string
printer_requeue_jobs_id_patch_request_instance = PrinterRequeueJobsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print PrinterRequeueJobsIdPatchRequest.to_json()

# convert the object into a dict
printer_requeue_jobs_id_patch_request_dict = printer_requeue_jobs_id_patch_request_instance.to_dict()
# create an instance of PrinterRequeueJobsIdPatchRequest from a dict
printer_requeue_jobs_id_patch_request_form_dict = printer_requeue_jobs_id_patch_request.from_dict(printer_requeue_jobs_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


