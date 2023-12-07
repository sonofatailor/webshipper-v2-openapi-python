# PrinterJobs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**completed** | **bool** | This will return as &lt;code&gt;true&lt;/code&gt; when the printer client has accepted the job. | [optional] 
**error** | **str** | Any error message that resulted. | [optional] 
**var_base64** | **str** | Base64 encoding if the associated printable, must the explicitly included in &lt;em&gt;fields&lt;/em&gt; query parameter to be included | [optional] [readonly] 
**try_count** | **int** |  | [optional] 
**initiator** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.printer_jobs import PrinterJobs

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterJobs from a JSON string
printer_jobs_instance = PrinterJobs.from_json(json)
# print the JSON string representation of the object
print PrinterJobs.to_json()

# convert the object into a dict
printer_jobs_dict = printer_jobs_instance.to_dict()
# create an instance of PrinterJobs from a dict
printer_jobs_form_dict = printer_jobs.from_dict(printer_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


