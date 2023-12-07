# ShippingRatesIdGet200ResponseIncludedInnerData


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
**carrier_id** | **int** | Id of the carrier which the shipping rate belongs to | [optional] [readonly] 
**order_channel_id** | **int** | Id of the order channel which the shipping rate belongs to | [optional] [readonly] 
**name** | **str** |  | [optional] 
**carrier_service_code** | **str** | The carrier&#39;s service code which must be used when generating parcels with this shipping rate. | [optional] 
**require_drop_point** | **bool** | Determines if the shipping rate requires a drop point to be assigned. | [optional] 
**visible_for** | **int** | Enum - determines whether the rate is returned for all customers, private_customers or business customers. This must be one of the following values:  &lt;code&gt;any&lt;/code&gt;, &lt;code&gt;privat_customers&lt;/code&gt;, &lt;code&gt;business_customers&lt;/code&gt; | [optional] 
**service_attributes** | **str** | Array of flattened resources of type &lt;code&gt;Service Attribute&lt;/code&gt;. Depends on the carrier service&#39;s requirements. Service Attribute has the following attributes:  &lt;code&gt;attr_key&lt;/code&gt;, &lt;code&gt;attr_value&lt;/code&gt;. You may use the Webshipper Template Language (WTL) for the values. | [optional] 
**dimensions** | **str** | Predefined dimensions which are a assigned when using the shipping rate. Attributes are: &lt;code&gt;height&lt;/code&gt;,&lt;code&gt;width&lt;/code&gt; and &lt;code&gt;length&lt;/code&gt;. The Webshipper Template Language (WTL) may be used for the values. | [optional] 
**add_ons** | **str** | Array of add_ons supported by the carrier service. | [optional] 
**is_return** | **bool** | Defines whether the rate is a return (inbound) rate or a standard rate (outbound). Please be aware that this attribute must match the carrier&#39;s service type. | [optional] 
**carriers_email** | **bool** | When this is set to true, the shipping rate will enable e-mail notifications from the carrier. | [optional] 
**comment_map** | **str** | Defines what content is included in the comment field. The Webshipper Template Language (WTL) may be used in this field. For example:  {{order.external_comment}} | [optional] 
**reference_map** | **str** | Defines what content is included in the reference field. The Webshipper Template Language (WTL) may be used in this field. For example: {{order.visible_ref}} | [optional] 
**carriers_sms** | **bool** | When this is set to true, the shipping rate will enable SMS notifications from the carrier. | [optional] 
**dutiable** | **bool** | Defines whether the goods sent using this shipping rate are dutiable. | [optional] 
**is_hidden** | **bool** | Attribute to indicate if the shipping rate is visible to order channels | [optional] 
**click_collect** | **bool** |  | [optional] 
**reference** | **str** |  | [optional] 
**default_colli_type** | **str** | Predefined colli type to be used when using the shipping rate. Must be supported by the carrier. | [optional] 
**sender_address_id** | **int** |  | [optional] 
**return_address_id** | **int** |  | [optional] 
**invoice_settings** | **str** |  | [optional] 
**shadow_booking_keep_labels** | **bool** |  | [optional] 
**shadow_booking_keep_documents** | **bool** |  | [optional] 
**ignore_rate_quote_validation** | **bool** |  | [optional] 
**custom_message** | **str** | Custom message to be displayed for the shipping rate | [optional] 
**regions** | **str** | Flattended array of Regions. See section on Shipping Regions and Expressions for more details | [optional] 
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

## Example

```python
from webshipperv2.models.shipping_rates_id_get200_response_included_inner_data import ShippingRatesIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingRatesIdGet200ResponseIncludedInnerData from a JSON string
shipping_rates_id_get200_response_included_inner_data_instance = ShippingRatesIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print ShippingRatesIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
shipping_rates_id_get200_response_included_inner_data_dict = shipping_rates_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of ShippingRatesIdGet200ResponseIncludedInnerData from a dict
shipping_rates_id_get200_response_included_inner_data_form_dict = shipping_rates_id_get200_response_included_inner_data.from_dict(shipping_rates_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


