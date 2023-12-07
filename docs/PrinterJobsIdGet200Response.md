# PrinterJobsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PrinterJobsIdGet200ResponseData**](PrinterJobsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**PrinterJobsIdGet200ResponseRelationships**](PrinterJobsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[PrinterJobsIdGet200ResponseIncludedInner]**](PrinterJobsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.printer_jobs_id_get200_response import PrinterJobsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterJobsIdGet200Response from a JSON string
printer_jobs_id_get200_response_instance = PrinterJobsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print PrinterJobsIdGet200Response.to_json()

# convert the object into a dict
printer_jobs_id_get200_response_dict = printer_jobs_id_get200_response_instance.to_dict()
# create an instance of PrinterJobsIdGet200Response from a dict
printer_jobs_id_get200_response_form_dict = printer_jobs_id_get200_response.from_dict(printer_jobs_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


