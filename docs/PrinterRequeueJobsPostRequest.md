# PrinterRequeueJobsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PrinterRequeueJobsPostRequestData**](PrinterRequeueJobsPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.printer_requeue_jobs_post_request import PrinterRequeueJobsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterRequeueJobsPostRequest from a JSON string
printer_requeue_jobs_post_request_instance = PrinterRequeueJobsPostRequest.from_json(json)
# print the JSON string representation of the object
print PrinterRequeueJobsPostRequest.to_json()

# convert the object into a dict
printer_requeue_jobs_post_request_dict = printer_requeue_jobs_post_request_instance.to_dict()
# create an instance of PrinterRequeueJobsPostRequest from a dict
printer_requeue_jobs_post_request_form_dict = printer_requeue_jobs_post_request.from_dict(printer_requeue_jobs_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


