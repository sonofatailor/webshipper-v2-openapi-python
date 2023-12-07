# PrinterJobsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PrinterJobsPostRequestData**](PrinterJobsPostRequestData.md) |  | [optional] 
**relationships** | [**PrinterJobsIdGet200ResponseRelationships**](PrinterJobsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.printer_jobs_post_request import PrinterJobsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterJobsPostRequest from a JSON string
printer_jobs_post_request_instance = PrinterJobsPostRequest.from_json(json)
# print the JSON string representation of the object
print PrinterJobsPostRequest.to_json()

# convert the object into a dict
printer_jobs_post_request_dict = printer_jobs_post_request_instance.to_dict()
# create an instance of PrinterJobsPostRequest from a dict
printer_jobs_post_request_form_dict = printer_jobs_post_request.from_dict(printer_jobs_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


