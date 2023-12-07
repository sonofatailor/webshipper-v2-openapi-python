# OrdersPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrdersPostRequestData**](OrdersPostRequestData.md) |  | [optional] 
**relationships** | [**OrdersIdGet200ResponseRelationships**](OrdersIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.orders_post_request import OrdersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersPostRequest from a JSON string
orders_post_request_instance = OrdersPostRequest.from_json(json)
# print the JSON string representation of the object
print OrdersPostRequest.to_json()

# convert the object into a dict
orders_post_request_dict = orders_post_request_instance.to_dict()
# create an instance of OrdersPostRequest from a dict
orders_post_request_form_dict = orders_post_request.from_dict(orders_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


