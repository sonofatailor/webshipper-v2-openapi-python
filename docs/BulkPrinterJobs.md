# BulkPrinterJobs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **str** |  | [optional] 
**model_type** | **str** |  | [optional] 
**printer_client_id** | **str** |  | [optional] 

## Example

```python
from webshipperv2.models.bulk_printer_jobs import BulkPrinterJobs

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPrinterJobs from a JSON string
bulk_printer_jobs_instance = BulkPrinterJobs.from_json(json)
# print the JSON string representation of the object
print BulkPrinterJobs.to_json()

# convert the object into a dict
bulk_printer_jobs_dict = bulk_printer_jobs_instance.to_dict()
# create an instance of BulkPrinterJobs from a dict
bulk_printer_jobs_form_dict = bulk_printer_jobs.from_dict(bulk_printer_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


