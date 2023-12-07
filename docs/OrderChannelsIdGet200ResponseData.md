# OrderChannelsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**OrderChannels**](OrderChannels.md) |  | [optional] 

## Example

```python
from webshipperv2.models.order_channels_id_get200_response_data import OrderChannelsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelsIdGet200ResponseData from a JSON string
order_channels_id_get200_response_data_instance = OrderChannelsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print OrderChannelsIdGet200ResponseData.to_json()

# convert the object into a dict
order_channels_id_get200_response_data_dict = order_channels_id_get200_response_data_instance.to_dict()
# create an instance of OrderChannelsIdGet200ResponseData from a dict
order_channels_id_get200_response_data_form_dict = order_channels_id_get200_response_data.from_dict(order_channels_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


