# OrdersPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Orders**](Orders.md) |  | [optional] 

## Example

```python
from openapi_client.models.orders_post_request_data import OrdersPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersPostRequestData from a JSON string
orders_post_request_data_instance = OrdersPostRequestData.from_json(json)
# print the JSON string representation of the object
print OrdersPostRequestData.to_json()

# convert the object into a dict
orders_post_request_data_dict = orders_post_request_data_instance.to_dict()
# create an instance of OrdersPostRequestData from a dict
orders_post_request_data_form_dict = orders_post_request_data.from_dict(orders_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


