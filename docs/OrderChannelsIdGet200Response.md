# OrderChannelsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrderChannelsIdGet200ResponseData**](OrderChannelsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**OrderChannelsIdGet200ResponseRelationships**](OrderChannelsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[OrderChannelsIdGet200ResponseIncludedInner]**](OrderChannelsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_channels_id_get200_response import OrderChannelsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannelsIdGet200Response from a JSON string
order_channels_id_get200_response_instance = OrderChannelsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print OrderChannelsIdGet200Response.to_json()

# convert the object into a dict
order_channels_id_get200_response_dict = order_channels_id_get200_response_instance.to_dict()
# create an instance of OrderChannelsIdGet200Response from a dict
order_channels_id_get200_response_form_dict = order_channels_id_get200_response.from_dict(order_channels_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


