# CarrierAccessesIdGet200ResponseIncludedInnerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Your name for the carrier | [optional] 
**services** | **str** | Array of services provided by this Carrier | [optional] 
**attrs** | **str** | Array of hashes with keys: &lt;code&gt;attr_key&lt;/code&gt;, &lt;code&gt;attr_value&lt;/code&gt;, &lt;code&gt;attr_name&lt;/code&gt;, &lt;code&gt;attr_type&lt;/code&gt;, &lt;code&gt;is_required&lt;/code&gt;, &lt;code&gt;only_visible_on_creation&lt;/code&gt;, &lt;/code&gt;enums&lt;/code&gt;. See       documentation for Local Attributes | [optional] 
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
**logo** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**print_error_label** | **bool** |  | [optional] 
**ftp_configuration_id** | **int** |  | [optional] 
**first_name** | **str** | The user&#39;s first name. | [optional] 
**last_name** | **str** | The user&#39;s last name. | [optional] 
**email** | **str** | The user&#39;s e-mail address. | [optional] 
**password** | **int** | The user&#39;s password. This can only be used for changing the password. | [optional] 
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
from webshipperv2.models.carrier_accesses_id_get200_response_included_inner_data import CarrierAccessesIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of CarrierAccessesIdGet200ResponseIncludedInnerData from a JSON string
carrier_accesses_id_get200_response_included_inner_data_instance = CarrierAccessesIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print CarrierAccessesIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
carrier_accesses_id_get200_response_included_inner_data_dict = carrier_accesses_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of CarrierAccessesIdGet200ResponseIncludedInnerData from a dict
carrier_accesses_id_get200_response_included_inner_data_form_dict = carrier_accesses_id_get200_response_included_inner_data.from_dict(carrier_accesses_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


