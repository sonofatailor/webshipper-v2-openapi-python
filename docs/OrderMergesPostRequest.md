# OrderMergesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrderMergesPostRequestData**](OrderMergesPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.order_merges_post_request import OrderMergesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderMergesPostRequest from a JSON string
order_merges_post_request_instance = OrderMergesPostRequest.from_json(json)
# print the JSON string representation of the object
print OrderMergesPostRequest.to_json()

# convert the object into a dict
order_merges_post_request_dict = order_merges_post_request_instance.to_dict()
# create an instance of OrderMergesPostRequest from a dict
order_merges_post_request_form_dict = order_merges_post_request.from_dict(order_merges_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


