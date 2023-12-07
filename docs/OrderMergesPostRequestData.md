# OrderMergesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**OrderMerges**](OrderMerges.md) |  | [optional] 

## Example

```python
from webshipperv2.models.order_merges_post_request_data import OrderMergesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of OrderMergesPostRequestData from a JSON string
order_merges_post_request_data_instance = OrderMergesPostRequestData.from_json(json)
# print the JSON string representation of the object
print OrderMergesPostRequestData.to_json()

# convert the object into a dict
order_merges_post_request_data_dict = order_merges_post_request_data_instance.to_dict()
# create an instance of OrderMergesPostRequestData from a dict
order_merges_post_request_data_form_dict = order_merges_post_request_data.from_dict(order_merges_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


