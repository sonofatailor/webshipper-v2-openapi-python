# ReturnPortals


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
from webshipperv2.models.return_portals import ReturnPortals

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnPortals from a JSON string
return_portals_instance = ReturnPortals.from_json(json)
# print the JSON string representation of the object
print ReturnPortals.to_json()

# convert the object into a dict
return_portals_dict = return_portals_instance.to_dict()
# create an instance of ReturnPortals from a dict
return_portals_form_dict = return_portals.from_dict(return_portals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


