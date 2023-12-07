# PrinterRequeueJobs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 
**job_id** | **str** |  | [optional] 
**mark_as_complete** | **str** |  | [optional] 

## Example

```python
from webshipperv2.models.printer_requeue_jobs import PrinterRequeueJobs

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterRequeueJobs from a JSON string
printer_requeue_jobs_instance = PrinterRequeueJobs.from_json(json)
# print the JSON string representation of the object
print PrinterRequeueJobs.to_json()

# convert the object into a dict
printer_requeue_jobs_dict = printer_requeue_jobs_instance.to_dict()
# create an instance of PrinterRequeueJobs from a dict
printer_requeue_jobs_form_dict = printer_requeue_jobs.from_dict(printer_requeue_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


