# BulkPrinterJobsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BulkPrinterJobsPostRequestData**](BulkPrinterJobsPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.bulk_printer_jobs_post_request import BulkPrinterJobsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPrinterJobsPostRequest from a JSON string
bulk_printer_jobs_post_request_instance = BulkPrinterJobsPostRequest.from_json(json)
# print the JSON string representation of the object
print BulkPrinterJobsPostRequest.to_json()

# convert the object into a dict
bulk_printer_jobs_post_request_dict = bulk_printer_jobs_post_request_instance.to_dict()
# create an instance of BulkPrinterJobsPostRequest from a dict
bulk_printer_jobs_post_request_form_dict = bulk_printer_jobs_post_request.from_dict(bulk_printer_jobs_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


