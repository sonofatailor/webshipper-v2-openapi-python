# PrinterRequeueJobsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PrinterRequeueJobsGet200ResponseDataInner]**](PrinterRequeueJobsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.printer_requeue_jobs_get200_response import PrinterRequeueJobsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterRequeueJobsGet200Response from a JSON string
printer_requeue_jobs_get200_response_instance = PrinterRequeueJobsGet200Response.from_json(json)
# print the JSON string representation of the object
print PrinterRequeueJobsGet200Response.to_json()

# convert the object into a dict
printer_requeue_jobs_get200_response_dict = printer_requeue_jobs_get200_response_instance.to_dict()
# create an instance of PrinterRequeueJobsGet200Response from a dict
printer_requeue_jobs_get200_response_form_dict = printer_requeue_jobs_get200_response.from_dict(printer_requeue_jobs_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


