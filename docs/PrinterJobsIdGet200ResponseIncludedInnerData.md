# PrinterJobsIdGet200ResponseIncludedInnerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique ID of the printer client | [optional] 
**approved** | **bool** | DEPRECATED | [optional] 
**alias** | **str** | Defaults to the host name of the machine running the client  | [optional] 
**is_online** | **bool** | Shows if the printer client is online | [optional] 
**last_connected** | **str** | Last connection time | [optional] 
**prevent_multiple_shipments** | **bool** |  | [optional] 
**name** | **str** | Name of the printer. | [optional] 
**active** | **bool** | Determines if the printer is configured on the printer station | [optional] 
**paper_width** | **float** | Paper width | [optional] 
**paper_height** | **float** | Paper height | [optional] 
**rotate_print_180** | **bool** |  | [optional] 

## Example

```python
from webshipperv2.models.printer_jobs_id_get200_response_included_inner_data import PrinterJobsIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterJobsIdGet200ResponseIncludedInnerData from a JSON string
printer_jobs_id_get200_response_included_inner_data_instance = PrinterJobsIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print PrinterJobsIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
printer_jobs_id_get200_response_included_inner_data_dict = printer_jobs_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of PrinterJobsIdGet200ResponseIncludedInnerData from a dict
printer_jobs_id_get200_response_included_inner_data_form_dict = printer_jobs_id_get200_response_included_inner_data.from_dict(printer_jobs_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


