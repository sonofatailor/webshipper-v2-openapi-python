# ReturnRefundMethodsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**ReturnRefundMethods**](ReturnRefundMethods.md) |  | [optional] 

## Example

```python
from webshipperv2.models.return_refund_methods_post_request_data import ReturnRefundMethodsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnRefundMethodsPostRequestData from a JSON string
return_refund_methods_post_request_data_instance = ReturnRefundMethodsPostRequestData.from_json(json)
# print the JSON string representation of the object
print ReturnRefundMethodsPostRequestData.to_json()

# convert the object into a dict
return_refund_methods_post_request_data_dict = return_refund_methods_post_request_data_instance.to_dict()
# create an instance of ReturnRefundMethodsPostRequestData from a dict
return_refund_methods_post_request_data_form_dict = return_refund_methods_post_request_data.from_dict(return_refund_methods_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


