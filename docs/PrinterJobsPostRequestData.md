# PrinterJobsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**PrinterJobs**](PrinterJobs.md) |  | [optional] 

## Example

```python
from webshipperv2.models.printer_jobs_post_request_data import PrinterJobsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterJobsPostRequestData from a JSON string
printer_jobs_post_request_data_instance = PrinterJobsPostRequestData.from_json(json)
# print the JSON string representation of the object
print PrinterJobsPostRequestData.to_json()

# convert the object into a dict
printer_jobs_post_request_data_dict = printer_jobs_post_request_data_instance.to_dict()
# create an instance of PrinterJobsPostRequestData from a dict
printer_jobs_post_request_data_form_dict = printer_jobs_post_request_data.from_dict(printer_jobs_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


