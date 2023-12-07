# BulkPrinterJobsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**BulkPrinterJobs**](BulkPrinterJobs.md) |  | [optional] 

## Example

```python
from openapi_client.models.bulk_printer_jobs_post_request_data import BulkPrinterJobsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPrinterJobsPostRequestData from a JSON string
bulk_printer_jobs_post_request_data_instance = BulkPrinterJobsPostRequestData.from_json(json)
# print the JSON string representation of the object
print BulkPrinterJobsPostRequestData.to_json()

# convert the object into a dict
bulk_printer_jobs_post_request_data_dict = bulk_printer_jobs_post_request_data_instance.to_dict()
# create an instance of BulkPrinterJobsPostRequestData from a dict
bulk_printer_jobs_post_request_data_form_dict = bulk_printer_jobs_post_request_data.from_dict(bulk_printer_jobs_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


