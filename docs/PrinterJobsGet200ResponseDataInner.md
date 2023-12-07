# PrinterJobsGet200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PrinterJobs**](PrinterJobs.md) |  | [optional] 

## Example

```python
from webshipperv2.models.printer_jobs_get200_response_data_inner import PrinterJobsGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterJobsGet200ResponseDataInner from a JSON string
printer_jobs_get200_response_data_inner_instance = PrinterJobsGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print PrinterJobsGet200ResponseDataInner.to_json()

# convert the object into a dict
printer_jobs_get200_response_data_inner_dict = printer_jobs_get200_response_data_inner_instance.to_dict()
# create an instance of PrinterJobsGet200ResponseDataInner from a dict
printer_jobs_get200_response_data_inner_form_dict = printer_jobs_get200_response_data_inner.from_dict(printer_jobs_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


