# OrderChannelsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**OrderChannels**](OrderChannels.md) |  | [optional] 

## Example

```python
from webshipperv2.models.order_channels_post_request_data import OrderChannelsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelsPostRequestData from a JSON string
order_channels_post_request_data_instance = OrderChannelsPostRequestData.from_json(json)
# print the JSON string representation of the object
print OrderChannelsPostRequestData.to_json()

# convert the object into a dict
order_channels_post_request_data_dict = order_channels_post_request_data_instance.to_dict()
# create an instance of OrderChannelsPostRequestData from a dict
order_channels_post_request_data_form_dict = order_channels_post_request_data.from_dict(order_channels_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


