# PrinterJobsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PrinterJobsIdGet200ResponseData**](PrinterJobsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**PrinterJobsIdGet200ResponseRelationships**](PrinterJobsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.printer_jobs_id_patch_request import PrinterJobsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterJobsIdPatchRequest from a JSON string
printer_jobs_id_patch_request_instance = PrinterJobsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print PrinterJobsIdPatchRequest.to_json()

# convert the object into a dict
printer_jobs_id_patch_request_dict = printer_jobs_id_patch_request_instance.to_dict()
# create an instance of PrinterJobsIdPatchRequest from a dict
printer_jobs_id_patch_request_form_dict = printer_jobs_id_patch_request.from_dict(printer_jobs_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


