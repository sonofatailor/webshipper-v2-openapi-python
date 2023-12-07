# PrinterRequeueJobsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PrinterRequeueJobsIdGet200ResponseData**](PrinterRequeueJobsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.printer_requeue_jobs_id_get200_response import PrinterRequeueJobsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterRequeueJobsIdGet200Response from a JSON string
printer_requeue_jobs_id_get200_response_instance = PrinterRequeueJobsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print PrinterRequeueJobsIdGet200Response.to_json()

# convert the object into a dict
printer_requeue_jobs_id_get200_response_dict = printer_requeue_jobs_id_get200_response_instance.to_dict()
# create an instance of PrinterRequeueJobsIdGet200Response from a dict
printer_requeue_jobs_id_get200_response_form_dict = printer_requeue_jobs_id_get200_response.from_dict(printer_requeue_jobs_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


