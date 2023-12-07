# OrdersIdGet200ResponseIncludedInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**data** | [**OrdersIdGet200ResponseIncludedInnerData**](OrdersIdGet200ResponseIncludedInnerData.md) |  | [optional] 

## Example

```python
from webshipperv2.models.orders_id_get200_response_included_inner import OrdersIdGet200ResponseIncludedInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersIdGet200ResponseIncludedInner from a JSON string
orders_id_get200_response_included_inner_instance = OrdersIdGet200ResponseIncludedInner.from_json(json)
# print the JSON string representation of the object
print OrdersIdGet200ResponseIncludedInner.to_json()

# convert the object into a dict
orders_id_get200_response_included_inner_dict = orders_id_get200_response_included_inner_instance.to_dict()
# create an instance of OrdersIdGet200ResponseIncludedInner from a dict
orders_id_get200_response_included_inner_form_dict = orders_id_get200_response_included_inner.from_dict(orders_id_get200_response_included_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


