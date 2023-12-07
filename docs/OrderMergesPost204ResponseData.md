# OrderMergesPost204ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**OrderMerges**](OrderMerges.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_merges_post204_response_data import OrderMergesPost204ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of OrderMergesPost204ResponseData from a JSON string
order_merges_post204_response_data_instance = OrderMergesPost204ResponseData.from_json(json)
# print the JSON string representation of the object
print OrderMergesPost204ResponseData.to_json()

# convert the object into a dict
order_merges_post204_response_data_dict = order_merges_post204_response_data_instance.to_dict()
# create an instance of OrderMergesPost204ResponseData from a dict
order_merges_post204_response_data_form_dict = order_merges_post204_response_data.from_dict(order_merges_post204_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


