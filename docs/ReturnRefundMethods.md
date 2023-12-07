# ReturnRefundMethods


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**allowed_days** | **int** |  | [optional] 

## Example

```python
from webshipperv2.models.return_refund_methods import ReturnRefundMethods

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnRefundMethods from a JSON string
return_refund_methods_instance = ReturnRefundMethods.from_json(json)
# print the JSON string representation of the object
print ReturnRefundMethods.to_json()

# convert the object into a dict
return_refund_methods_dict = return_refund_methods_instance.to_dict()
# create an instance of ReturnRefundMethods from a dict
return_refund_methods_form_dict = return_refund_methods.from_dict(return_refund_methods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


