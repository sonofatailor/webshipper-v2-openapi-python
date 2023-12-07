# ReturnRefundMethodsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReturnRefundMethodsPostRequestData**](ReturnRefundMethodsPostRequestData.md) |  | [optional] 
**relationships** | [**ReturnRefundMethodsIdGet200ResponseRelationships**](ReturnRefundMethodsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.return_refund_methods_post_request import ReturnRefundMethodsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnRefundMethodsPostRequest from a JSON string
return_refund_methods_post_request_instance = ReturnRefundMethodsPostRequest.from_json(json)
# print the JSON string representation of the object
print ReturnRefundMethodsPostRequest.to_json()

# convert the object into a dict
return_refund_methods_post_request_dict = return_refund_methods_post_request_instance.to_dict()
# create an instance of ReturnRefundMethodsPostRequest from a dict
return_refund_methods_post_request_form_dict = return_refund_methods_post_request.from_dict(return_refund_methods_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


