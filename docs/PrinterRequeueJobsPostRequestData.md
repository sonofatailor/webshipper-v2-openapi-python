# PrinterRequeueJobsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**PrinterRequeueJobs**](PrinterRequeueJobs.md) |  | [optional] 

## Example

```python
from openapi_client.models.printer_requeue_jobs_post_request_data import PrinterRequeueJobsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterRequeueJobsPostRequestData from a JSON string
printer_requeue_jobs_post_request_data_instance = PrinterRequeueJobsPostRequestData.from_json(json)
# print the JSON string representation of the object
print PrinterRequeueJobsPostRequestData.to_json()

# convert the object into a dict
printer_requeue_jobs_post_request_data_dict = printer_requeue_jobs_post_request_data_instance.to_dict()
# create an instance of PrinterRequeueJobsPostRequestData from a dict
printer_requeue_jobs_post_request_data_form_dict = printer_requeue_jobs_post_request_data.from_dict(printer_requeue_jobs_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


