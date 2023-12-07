# BulkPrinterJobsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BulkPrinterJobsIdGet200ResponseData**](BulkPrinterJobsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.bulk_printer_jobs_id_get200_response import BulkPrinterJobsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPrinterJobsIdGet200Response from a JSON string
bulk_printer_jobs_id_get200_response_instance = BulkPrinterJobsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print BulkPrinterJobsIdGet200Response.to_json()

# convert the object into a dict
bulk_printer_jobs_id_get200_response_dict = bulk_printer_jobs_id_get200_response_instance.to_dict()
# create an instance of BulkPrinterJobsIdGet200Response from a dict
bulk_printer_jobs_id_get200_response_form_dict = bulk_printer_jobs_id_get200_response.from_dict(bulk_printer_jobs_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


