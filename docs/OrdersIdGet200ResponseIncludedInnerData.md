# OrdersIdGet200ResponseIncludedInnerData


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
**carrier_id** | **int** | Id of the carrier which the shipping rate belongs to | [optional] [readonly] 
**order_channel_id** | **int** | Id of the order channel which the shipping rate belongs to | [optional] [readonly] 
**name** | **str** | Name to be displayed in the e-commerce system. | [optional] 
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
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**default_colli_type** | **str** | Predefined colli type to be used when using the shipping rate. Must be supported by the carrier. | [optional] 
**sender_address_id** | **int** |  | [optional] 
**return_address_id** | **int** |  | [optional] 
**invoice_settings** | **str** |  | [optional] 
**shadow_booking_keep_labels** | **bool** |  | [optional] 
**shadow_booking_keep_documents** | **bool** |  | [optional] 
**ignore_rate_quote_validation** | **bool** |  | [optional] 
**custom_message** | **str** | Custom message to be displayed for the shipping rate | [optional] 
**regions** | **str** | Flattended array of Regions. See section on Shipping Regions and Expressions for more details | [optional] 
**translations** | **str** |  | [optional] 
**matcher** | **str** |  | [optional] 
**error_class** | **str** |  | [optional] 
**support_url** | **str** |  | [optional] 
**uuid** | **str** | Unique ID of the printer client | [optional] 
**approved** | **bool** | DEPRECATED | [optional] 
**alias** | **str** | Defaults to the host name of the machine running the client  | [optional] 
**is_online** | **bool** | Shows if the printer client is online | [optional] 
**last_connected** | **str** | Shows when the printer client was last connected | [optional] 
**prevent_multiple_shipments** | **bool** |  | [optional] 

## Example

```python
from webshipperv2.models.orders_id_get200_response_included_inner_data import OrdersIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersIdGet200ResponseIncludedInnerData from a JSON string
orders_id_get200_response_included_inner_data_instance = OrdersIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print OrdersIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
orders_id_get200_response_included_inner_data_dict = orders_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of OrdersIdGet200ResponseIncludedInnerData from a dict
orders_id_get200_response_included_inner_data_form_dict = orders_id_get200_response_included_inner_data.from_dict(orders_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


