# CsvMappingsIdGet200ResponseIncludedInnerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Your name for the carrier | [optional] 
**services** | **str** | Array of services provided by this Carrier | [optional] 
**attrs** | **List[str]** | Array of hashed with keys: &lt;code&gt;attr_key&lt;/code&gt;, &lt;code&gt;attr_value&lt;/code&gt;, &lt;code&gt;attr_name&lt;/code&gt;, &lt;code&gt;attr_type&lt;/code&gt;, &lt;code&gt;is_required&lt;/code&gt;, &lt;code&gt;only_visible_on_creation&lt;/code&gt; &lt;/code&gt;enums&lt;/code&gt;. See       documentation for Local Attributes | [optional] 
**prefer_zpl** | **bool** |  | [optional] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**is_approved** | **bool** |  | [optional] 
**approved_service_codes** | **str** |  | [optional] 
**service_parameter_enums** | **str** |  | [optional] 
**barcode_notification_behavior** | **int** |  | [optional] 
**barcode_notification_mail** | **str** |  | [optional] 
**has_active_cost_sheet** | **str** |  | [optional] 
**delete_at_carrier** | **bool** |  | [optional] 
**test_mode** | **bool** |  | [optional] 
**logo** | **str** | Base64 representation of the logo of the order channel. | [optional] 
**logo_url** | **str** |  | [optional] 
**print_error_label** | **bool** |  | [optional] 
**ftp_configuration_id** | **int** |  | [optional] 
**channel_label** | **str** | Label to identify the order channel. | [optional] 
**additional_parameters** | **object** | Optional hash, this is used when creating new order channels. | [optional] 
**slip_print_mode** | **str** | Possible values: &#39;dont_print&#39;, &#39;print_immediately&#39; or &#39;print_with_shipment&#39;. | [optional] 
**return_label_print_mode** | **str** | Possible values: &#39;dont_print&#39;, &#39;print_immediately&#39;. | [optional] 
**shipping_label_print_mode** | **str** | Possible values: &#39;dont_print&#39;, &#39;print_immediately&#39;. | [optional] 
**document_print_mode** | **str** | Possible values: &#39;dont_print&#39;, &#39;print_immediately&#39;. | [optional] 
**configuration_token** | **str** | Token to use for Webshipper modules. Tokens will only be generated for modules that require a configuration token. | [optional] 
**sync_status** | **int** | Determines if the order channel is currently synchronising. Possible values are: &lt;code&gt;synchronize&lt;/code&gt;, &lt;code&gt;suspended&lt;/code&gt;, &lt;code&gt;paused&lt;/code&gt;. | [optional] 
**failed_sync_count** | **int** | Shows if recent synchronisation events have failed. | [optional] 
**fulfill_automatically** | **bool** | Whether or not to fulfill the order in the original order channel when a shipment is created. Default: true | [optional] 
**drop_point_limit** | **int** |  | [optional] 
**create_shipment_automatically** | **bool** |  | [optional] 
**health** | **str** |  | [optional] 
**convert_currency_on_rate_quotes** | **bool** |  | [optional] 
**sync_additional_attributes_to_shipments** | **bool** |  | [optional] 
**auto_order_import** | **bool** |  | [optional] 

## Example

```python
from webshipperv2.models.csv_mappings_id_get200_response_included_inner_data import CsvMappingsIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of CsvMappingsIdGet200ResponseIncludedInnerData from a JSON string
csv_mappings_id_get200_response_included_inner_data_instance = CsvMappingsIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print CsvMappingsIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
csv_mappings_id_get200_response_included_inner_data_dict = csv_mappings_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of CsvMappingsIdGet200ResponseIncludedInnerData from a dict
csv_mappings_id_get200_response_included_inner_data_form_dict = csv_mappings_id_get200_response_included_inner_data.from_dict(csv_mappings_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


