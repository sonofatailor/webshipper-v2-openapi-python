# OrderChannelTypesIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**OrderChannelTypes**](OrderChannelTypes.md) |  | [optional] 

## Example

```python
from webshipperv2.models.order_channel_types_id_get200_response_data import OrderChannelTypesIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelTypesIdGet200ResponseData from a JSON string
order_channel_types_id_get200_response_data_instance = OrderChannelTypesIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print OrderChannelTypesIdGet200ResponseData.to_json()

# convert the object into a dict
order_channel_types_id_get200_response_data_dict = order_channel_types_id_get200_response_data_instance.to_dict()
# create an instance of OrderChannelTypesIdGet200ResponseData from a dict
order_channel_types_id_get200_response_data_form_dict = order_channel_types_id_get200_response_data.from_dict(order_channel_types_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


