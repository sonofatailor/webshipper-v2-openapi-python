# OrderChannelsIdGet200ResponseIncludedInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**data** | [**OrderChannelsIdGet200ResponseIncludedInnerData**](OrderChannelsIdGet200ResponseIncludedInnerData.md) |  | [optional] 

## Example

```python
from webshipperv2.models.order_channels_id_get200_response_included_inner import OrderChannelsIdGet200ResponseIncludedInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelsIdGet200ResponseIncludedInner from a JSON string
order_channels_id_get200_response_included_inner_instance = OrderChannelsIdGet200ResponseIncludedInner.from_json(json)
# print the JSON string representation of the object
print OrderChannelsIdGet200ResponseIncludedInner.to_json()

# convert the object into a dict
order_channels_id_get200_response_included_inner_dict = order_channels_id_get200_response_included_inner_instance.to_dict()
# create an instance of OrderChannelsIdGet200ResponseIncludedInner from a dict
order_channels_id_get200_response_included_inner_form_dict = order_channels_id_get200_response_included_inner.from_dict(order_channels_id_get200_response_included_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


