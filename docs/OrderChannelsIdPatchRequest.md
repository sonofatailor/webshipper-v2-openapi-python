# OrderChannelsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrderChannelsIdGet200ResponseData**](OrderChannelsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**OrderChannelsIdGet200ResponseRelationships**](OrderChannelsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.order_channels_id_patch_request import OrderChannelsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelsIdPatchRequest from a JSON string
order_channels_id_patch_request_instance = OrderChannelsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print OrderChannelsIdPatchRequest.to_json()

# convert the object into a dict
order_channels_id_patch_request_dict = order_channels_id_patch_request_instance.to_dict()
# create an instance of OrderChannelsIdPatchRequest from a dict
order_channels_id_patch_request_form_dict = order_channels_id_patch_request.from_dict(order_channels_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


