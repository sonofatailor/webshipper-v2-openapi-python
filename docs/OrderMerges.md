# OrderMerges


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **bool** | ID of order to merge order lines in to | [optional] 
**orders** | **List[str]** | Orders from which to merge order lines from. Orders as nested resources | [optional] 

## Example

```python
from webshipperv2.models.order_merges import OrderMerges

# TODO update the JSON string below
json = "{}"
# create an instance of OrderMerges from a JSON string
order_merges_instance = OrderMerges.from_json(json)
# print the JSON string representation of the object
print OrderMerges.to_json()

# convert the object into a dict
order_merges_dict = order_merges_instance.to_dict()
# create an instance of OrderMerges from a dict
order_merges_form_dict = order_merges.from_dict(order_merges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


