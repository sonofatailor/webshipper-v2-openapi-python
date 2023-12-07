# ReturnRefundMethodsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReturnRefundMethodsIdGet200ResponseData**](ReturnRefundMethodsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**ReturnRefundMethodsIdGet200ResponseRelationships**](ReturnRefundMethodsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.return_refund_methods_id_patch_request import ReturnRefundMethodsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnRefundMethodsIdPatchRequest from a JSON string
return_refund_methods_id_patch_request_instance = ReturnRefundMethodsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ReturnRefundMethodsIdPatchRequest.to_json()

# convert the object into a dict
return_refund_methods_id_patch_request_dict = return_refund_methods_id_patch_request_instance.to_dict()
# create an instance of ReturnRefundMethodsIdPatchRequest from a dict
return_refund_methods_id_patch_request_form_dict = return_refund_methods_id_patch_request.from_dict(return_refund_methods_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


