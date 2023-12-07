# ReturnPortalsIdGet200ResponseIncludedInnerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_label** | **str** | Label to identify the order channel. | [optional] 
**attrs** | **List[str]** | Array of hashed with keys: &lt;code&gt;attr_key&lt;/code&gt;, &lt;code&gt;attr_value&lt;/code&gt;, &lt;code&gt;attr_name&lt;/code&gt;, &lt;code&gt;attr_type&lt;/code&gt;, &lt;code&gt;is_required&lt;/code&gt;, &lt;code&gt;only_visible_on_creation&lt;/code&gt; &lt;/code&gt;enums&lt;/code&gt;. See       documentation for Local Attributes | [optional] 
**additional_parameters** | **object** | Optional hash, this is used when creating new order channels. | [optional] 
**slip_print_mode** | **str** | Possible values: &#39;dont_print&#39;, &#39;print_immediately&#39; or &#39;print_with_shipment&#39;. | [optional] 
**return_label_print_mode** | **str** | Possible values: &#39;dont_print&#39;, &#39;print_immediately&#39;. | [optional] 
**shipping_label_print_mode** | **str** | Possible values: &#39;dont_print&#39;, &#39;print_immediately&#39;. | [optional] 
**document_print_mode** | **str** | Possible values: &#39;dont_print&#39;, &#39;print_immediately&#39;. | [optional] 
**logo** | **str** | Base64 representation of the logo of the order channel. | [optional] 
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
**name** | **str** |  | [optional] 
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
**default_locale** | **str** |  | [optional] 
**mail_locales** | **str** |  | [optional] 
**images** | **str** |  | [optional] 
**purpose** | **int** |  | [optional] 
**bcc_mail** | **str** |  | [optional] 
**is_prebuilt** | **bool** |  | [optional] 
**overrides** | **str** |  | [optional] 
**defaults** | **str** |  | [optional] 
**hook** | **str** |  | [optional] 
**whitelisted_languages** | **str** |  | [optional] 
**described** | **str** | Encapsulated with new WYSIWYG editor and legacy HTML based templates | [optional] [readonly] 
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

## Example

```python
from openapi_client.models.return_portals_id_get200_response_included_inner_data import ReturnPortalsIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnPortalsIdGet200ResponseIncludedInnerData from a JSON string
return_portals_id_get200_response_included_inner_data_instance = ReturnPortalsIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print ReturnPortalsIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
return_portals_id_get200_response_included_inner_data_dict = return_portals_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of ReturnPortalsIdGet200ResponseIncludedInnerData from a dict
return_portals_id_get200_response_included_inner_data_form_dict = return_portals_id_get200_response_included_inner_data.from_dict(return_portals_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


