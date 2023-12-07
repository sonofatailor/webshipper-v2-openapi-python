# HotKeysIdGet200ResponseIncludedInnerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path of the favourite page | [optional] 
**name** | **str** | Name of the favourite page | [optional] 
**user_id** | **int** |  | [optional] 
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
from webshipperv2.models.hot_keys_id_get200_response_included_inner_data import HotKeysIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of HotKeysIdGet200ResponseIncludedInnerData from a JSON string
hot_keys_id_get200_response_included_inner_data_instance = HotKeysIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print HotKeysIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
hot_keys_id_get200_response_included_inner_data_dict = hot_keys_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of HotKeysIdGet200ResponseIncludedInnerData from a dict
hot_keys_id_get200_response_included_inner_data_form_dict = hot_keys_id_get200_response_included_inner_data.from_dict(hot_keys_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


