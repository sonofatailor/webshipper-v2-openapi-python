# OrderChannelAccessesIdGet200ResponseIncludedInnerData


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
**first_name** | **str** | The user&#39;s first name. | [optional] 
**last_name** | **str** | The user&#39;s last name. | [optional] 
**email** | **str** | The user&#39;s e-mail address. | [optional] 
**password** | **int** | The user&#39;s password. This can only be used for changing the password. | [optional] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**last_sign_in_at** | **str** | The time of the most recent sign-in by the user. | [optional] 
**all_order_channels** | **bool** | Specifies whether the user has access to all order channels on the tenant. | [optional] 
**all_carriers** | **bool** | Specifies whether the user has access to all of the carriers for tenant. | [optional] 
**hidden** | **bool** | Specifies whether the user should be hidden in the user interface. | [optional] 
**current_password** | **str** | This must be set when changing the password of the user. | [optional] 
**locale** | **int** | Locale enum. &lt;code&gt;da&lt;/code&gt; or &lt;code&gt;en&lt;/code&gt; | [optional] 
**locked_until** | **str** | Locked until specified datetime | [optional] 
**failed_count** | **int** | Amount of failed login attempts since last login | [optional] 
**is_locked** | **str** | Read only. Will be true when the user is temporarily locked due to too many login attempts | [optional] 
**user_status** | **int** |  | [optional] 
**home_page** | **str** | The home page set by the user | [optional] 
**limit_order_search** | **str** |  | [optional] 
**view_ids** | **bool** | Allow user to see id&#39;s | [optional] 

## Example

```python
from webshipperv2.models.order_channel_accesses_id_get200_response_included_inner_data import OrderChannelAccessesIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelAccessesIdGet200ResponseIncludedInnerData from a JSON string
order_channel_accesses_id_get200_response_included_inner_data_instance = OrderChannelAccessesIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print OrderChannelAccessesIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
order_channel_accesses_id_get200_response_included_inner_data_dict = order_channel_accesses_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of OrderChannelAccessesIdGet200ResponseIncludedInnerData from a dict
order_channel_accesses_id_get200_response_included_inner_data_form_dict = order_channel_accesses_id_get200_response_included_inner_data.from_dict(order_channel_accesses_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


