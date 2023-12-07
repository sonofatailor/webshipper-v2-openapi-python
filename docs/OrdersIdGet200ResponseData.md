# OrdersIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Orders**](Orders.md) |  | [optional] 

## Example

```python
from webshipperv2.models.orders_id_get200_response_data import OrdersIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersIdGet200ResponseData from a JSON string
orders_id_get200_response_data_instance = OrdersIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print OrdersIdGet200ResponseData.to_json()

# convert the object into a dict
orders_id_get200_response_data_dict = orders_id_get200_response_data_instance.to_dict()
# create an instance of OrdersIdGet200ResponseData from a dict
orders_id_get200_response_data_form_dict = orders_id_get200_response_data.from_dict(orders_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


