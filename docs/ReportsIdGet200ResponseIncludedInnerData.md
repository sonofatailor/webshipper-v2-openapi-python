# ReportsIdGet200ResponseIncludedInnerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**columns** | **List[str]** | Array of objects with keys &lt;code&gt;header&lt;/code&gt; and &lt;code&gt;content&lt;/code&gt; | [optional] 
**parameters** | **List[str]** | Array of objects with keys &lt;code&gt;parameter_key&lt;/code&gt; and &lt;code&gt;parameter_value&lt;/code&gt; | [optional] 
**resource** | **str** |  | [optional] 
**header_columns** | **List[str]** | Array of objects with keys &lt;code&gt;header&lt;/code&gt; and &lt;code&gt;content&lt;/code&gt; that will be used to display the header content of the report | [optional] 
**footer_content** | **str** |  | [optional] 
**conditions** | **List[str]** | Array of objects describing how to load the resources. Contains keys &lt;code&gt;condition_key&lt;/code&gt;, &lt;code&gt;condition_operator&lt;/code&gt;, &lt;code&gt;condition_value&lt;/code&gt;. | [optional] 
**include_deleted** | **bool** | If true the report will included deleted records. Default: &lt;code&gt;false&lt;/code&gt; | [optional] 
**use_carrier_eod** | **bool** | When set to true it will attempt to fetch the end of day list directly from the carrier. When this option is enabled, only pdf reports are available. | [optional] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**schedule** | **str** |  | [optional] 
**default_format** | **str** |  | [optional] 
**mail_on_run** | **bool** |  | [optional] 
**mail** | **str** |  | [optional] 
**alias** | **str** | Your name for the carrier | [optional] 
**services** | **str** | Array of services provided by this Carrier | [optional] 
**attrs** | **str** | Array of hashes with keys: &lt;code&gt;attr_key&lt;/code&gt;, &lt;code&gt;attr_value&lt;/code&gt;, &lt;code&gt;attr_name&lt;/code&gt;, &lt;code&gt;attr_type&lt;/code&gt;, &lt;code&gt;is_required&lt;/code&gt;, &lt;code&gt;only_visible_on_creation&lt;/code&gt;, &lt;/code&gt;enums&lt;/code&gt;. See       documentation for Local Attributes | [optional] 
**prefer_zpl** | **bool** |  | [optional] 
**is_approved** | **bool** |  | [optional] 
**approved_service_codes** | **str** |  | [optional] 
**service_parameter_enums** | **str** |  | [optional] 
**barcode_notification_behavior** | **int** |  | [optional] 
**barcode_notification_mail** | **str** |  | [optional] 
**has_active_cost_sheet** | **str** |  | [optional] 
**delete_at_carrier** | **bool** |  | [optional] 
**test_mode** | **bool** |  | [optional] 
**logo** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**print_error_label** | **bool** |  | [optional] 
**ftp_configuration_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.reports_id_get200_response_included_inner_data import ReportsIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of ReportsIdGet200ResponseIncludedInnerData from a JSON string
reports_id_get200_response_included_inner_data_instance = ReportsIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print ReportsIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
reports_id_get200_response_included_inner_data_dict = reports_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of ReportsIdGet200ResponseIncludedInnerData from a dict
reports_id_get200_response_included_inner_data_form_dict = reports_id_get200_response_included_inner_data.from_dict(reports_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


