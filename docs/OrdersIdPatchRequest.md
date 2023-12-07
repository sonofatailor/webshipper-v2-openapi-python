# OrdersIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrdersIdGet200ResponseData**](OrdersIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**OrdersIdGet200ResponseRelationships**](OrdersIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.orders_id_patch_request import OrdersIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersIdPatchRequest from a JSON string
orders_id_patch_request_instance = OrdersIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print OrdersIdPatchRequest.to_json()

# convert the object into a dict
orders_id_patch_request_dict = orders_id_patch_request_instance.to_dict()
# create an instance of OrdersIdPatchRequest from a dict
orders_id_patch_request_form_dict = orders_id_patch_request.from_dict(orders_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


