# OrderMergesPost204Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrderMergesPost204ResponseData**](OrderMergesPost204ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.order_merges_post204_response import OrderMergesPost204Response

# TODO update the JSON string below
json = "{}"
# create an instance of OrderMergesPost204Response from a JSON string
order_merges_post204_response_instance = OrderMergesPost204Response.from_json(json)
# print the JSON string representation of the object
print OrderMergesPost204Response.to_json()

# convert the object into a dict
order_merges_post204_response_dict = order_merges_post204_response_instance.to_dict()
# create an instance of OrderMergesPost204Response from a dict
order_merges_post204_response_form_dict = order_merges_post204_response.from_dict(order_merges_post204_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


