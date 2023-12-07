# Reports


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**start_time** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 
**output_formats** | **List[str]** |  | [optional] 
**parameters** | **object** |  | [optional] 
**var_base64** | **str** |  | [optional] [readonly] 
**pdf_download_url** | **str** |  | [optional] 
**xml_download_url** | **str** |  | [optional] 
**csv_download_url** | **str** |  | [optional] 
**json_download_url** | **str** |  | [optional] 
**xlsx_download_url** | **str** |  | [optional] 
**failed** | **bool** |  | [optional] 
**order_ids** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from webshipperv2.models.reports import Reports

# TODO update the JSON string below
json = "{}"
# create an instance of Reports from a JSON string
reports_instance = Reports.from_json(json)
# print the JSON string representation of the object
print Reports.to_json()

# convert the object into a dict
reports_dict = reports_instance.to_dict()
# create an instance of Reports from a dict
reports_form_dict = reports.from_dict(reports_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


