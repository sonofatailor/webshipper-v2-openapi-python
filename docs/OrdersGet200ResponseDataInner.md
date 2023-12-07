# OrdersGet200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Orders**](Orders.md) |  | [optional] 

## Example

```python
from webshipperv2.models.orders_get200_response_data_inner import OrdersGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersGet200ResponseDataInner from a JSON string
orders_get200_response_data_inner_instance = OrdersGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print OrdersGet200ResponseDataInner.to_json()

# convert the object into a dict
orders_get200_response_data_inner_dict = orders_get200_response_data_inner_instance.to_dict()
# create an instance of OrdersGet200ResponseDataInner from a dict
orders_get200_response_data_inner_form_dict = orders_get200_response_data_inner.from_dict(orders_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


