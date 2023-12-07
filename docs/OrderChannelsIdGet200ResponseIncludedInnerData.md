# OrderChannelsIdGet200ResponseIncludedInnerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name to identify the template. | [optional] 
**support_url** | **str** |  | [optional] 
**public_global_attrs** | **str** |  | [optional] 
**list_logo** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**module_link** | **str** |  | [optional] 
**can_autofulfill** | **bool** |  | [optional] 
**can_limit_drop_points** | **bool** |  | [optional] 
**supports_rate_quoting** | **bool** |  | [optional] 
**uses_scheduled_import** | **bool** |  | [optional] 
**supports_time_interval_import** | **bool** |  | [optional] 
**supports_statuses_import** | **bool** |  | [optional] 
**supports_id_import** | **bool** |  | [optional] 
**supports_vat_in_checkout** | **bool** |  | [optional] 
**slip_size** | **int** | Size of the parcel slip. Possible values: &lt;code&gt;A4&lt;/code&gt; and &lt;code&gt;4X6&lt;/code&gt; | [optional] 
**additional_content** | **str** | Content after the table of order lines for A4-based parcel slips. | [optional] 
**additional_content_align** | **int** | Alignment of additional_content. Possible values: &lt;code&gt;center&lt;/code&gt;, &lt;code&gt;right&lt;/code&gt;, &lt;code&gt;left&lt;/code&gt; | [optional] 
**barcode_content** | **str** | Content of the barcode | [optional] 
**header_content** | **str** | Content of the slip header | [optional] 
**top_left_content_header** | **str** | Header of the top left corner | [optional] 
**top_right_content_header** | **str** | Header of the top right corner | [optional] 
**top_left_content** | **str** | Content of the top left corner | [optional] 
**top_right_content** | **str** | Content of the top right corner | [optional] 
**footer_content** | **str** | Content of the footer | [optional] 
**slip_template_columns** | **str** | Array of columns. Column objects contains: &lt;code&gt;name&lt;/code&gt;&lt;code&gt;content&lt;/code&gt;, &lt;code&gt;text_alignment&lt;/code&gt;(right, left, center), &lt;code&gt;width&lt;/code&gt; (in percentage) | [optional] 
**table_color** | **str** | HEX color including # | [optional] 
**table_text_color** | **str** | HEX color including # | [optional] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**sort_key** | **str** | The key to sort the order-lines by | [optional] 
**returns_only** | **bool** |  | [optional] 
**disable_inline_formatting** | **bool** |  | [optional] 
**att_contact** | **str** | Att person. To generate parcels either att_contact &lt;strong&gt;or&lt;/strong&gt; company_name is required | [optional] 
**company_name** | **str** | Company name. To generate parcels either att_contact &lt;strong&gt;or&lt;/strong&gt; company_name is required | [optional] 
**address_1** | **str** | Address line 1 | [optional] 
**address_2** | **str** | Address line 2 | [optional] 
**country_code** | **str** | ISO 3166-1 alpha-2 code | [optional] 
**state** | **str** | Sub-division of country, if applicable. State code. ISO 3166-2 alpha-2 | [optional] 
**phone** | **str** | Phone number of the entity. This can be used for SMS notifications. | [optional] 
**email** | **str** | E-mail address of the entity. This can be used for e-mail notifications. | [optional] 
**zip** | **str** | Postal code of the entity. This is required for most destination countries. | [optional] 
**city** | **str** | City of the entity. This is required for most destination countries. | [optional] 
**vat_no** | **str** | The VAT number of the entity. This is only required for address_type &lt;code&gt;sold_from&lt;/code&gt; | [optional] 
**address_type** | **str** | Used for special addresses for order channels. This will be one of the following: &lt;code&gt;recipient&lt;/code&gt;, &lt;code&gt;sender&lt;/code&gt;, &lt;code&gt;sold_from&lt;/code&gt;, &lt;code&gt;pickup&lt;/code&gt;, &lt;code&gt;return&lt;/code&gt;, &lt;code&gt;order_address&lt;/code&gt; | [optional] 
**ext_location** | **str** |  | [optional] 
**voec** | **str** |  | [optional] 
**eori** | **str** |  | [optional] 
**sprn** | **str** |  | [optional] 
**ioss** | **str** |  | [optional] 
**fda** | **str** |  | [optional] 
**duns** | **str** |  | [optional] 
**personal_customs_no** | **str** |  | [optional] 
**company_customs_numbers** | **str** |  | [optional] 
**uuid** | **str** | Unique ID of the printer client | [optional] 
**approved** | **bool** | DEPRECATED | [optional] 
**alias** | **str** | Defaults to the host name of the machine running the client  | [optional] 
**is_online** | **bool** | Shows if the printer client is online | [optional] 
**last_connected** | **str** | Shows when the printer client was last connected | [optional] 
**prevent_multiple_shipments** | **bool** |  | [optional] 

## Example

```python
from webshipperv2.models.order_channels_id_get200_response_included_inner_data import OrderChannelsIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelsIdGet200ResponseIncludedInnerData from a JSON string
order_channels_id_get200_response_included_inner_data_instance = OrderChannelsIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print OrderChannelsIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
order_channels_id_get200_response_included_inner_data_dict = order_channels_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of OrderChannelsIdGet200ResponseIncludedInnerData from a dict
order_channels_id_get200_response_included_inner_data_form_dict = order_channels_id_get200_response_included_inner_data.from_dict(order_channels_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


