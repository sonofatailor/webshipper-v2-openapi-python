# ReturnRefundMethodsIdGet200ResponseIncludedInnerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**custom_style** | **str** |  | [optional] 
**shipping_methods** | **str** |  | [optional] 
**translations** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**allowed_days_since_dispatch** | **int** |  | [optional] 
**send_immediately** | **bool** |  | [optional] 
**static_notice_email** | **str** |  | [optional] 
**order_channel_logo** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**force_single_page** | **bool** |  | [optional] 
**order_channel_id** | **int** |  | [optional] 
**optional_return_cause** | **bool** |  | [optional] 
**new_mail_template** | **str** |  | [optional] 
**new_confirmation_mail_template** | **str** |  | [optional] 

## Example

```python
from webshipperv2.models.return_refund_methods_id_get200_response_included_inner_data import ReturnRefundMethodsIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnRefundMethodsIdGet200ResponseIncludedInnerData from a JSON string
return_refund_methods_id_get200_response_included_inner_data_instance = ReturnRefundMethodsIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print ReturnRefundMethodsIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
return_refund_methods_id_get200_response_included_inner_data_dict = return_refund_methods_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of ReturnRefundMethodsIdGet200ResponseIncludedInnerData from a dict
return_refund_methods_id_get200_response_included_inner_data_form_dict = return_refund_methods_id_get200_response_included_inner_data.from_dict(return_refund_methods_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


