# OrdersIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrdersIdGet200ResponseData**](OrdersIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**OrdersIdGet200ResponseRelationships**](OrdersIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[OrdersIdGet200ResponseIncludedInner]**](OrdersIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.orders_id_get200_response import OrdersIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersIdGet200Response from a JSON string
orders_id_get200_response_instance = OrdersIdGet200Response.from_json(json)
# print the JSON string representation of the object
print OrdersIdGet200Response.to_json()

# convert the object into a dict
orders_id_get200_response_dict = orders_id_get200_response_instance.to_dict()
# create an instance of OrdersIdGet200Response from a dict
orders_id_get200_response_form_dict = orders_id_get200_response.from_dict(orders_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


