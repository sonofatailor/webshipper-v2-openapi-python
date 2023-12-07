# ReturnRefundMethodsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReturnRefundMethodsIdGet200ResponseData**](ReturnRefundMethodsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**ReturnRefundMethodsIdGet200ResponseRelationships**](ReturnRefundMethodsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[ReturnRefundMethodsIdGet200ResponseIncludedInner]**](ReturnRefundMethodsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.return_refund_methods_id_get200_response import ReturnRefundMethodsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnRefundMethodsIdGet200Response from a JSON string
return_refund_methods_id_get200_response_instance = ReturnRefundMethodsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print ReturnRefundMethodsIdGet200Response.to_json()

# convert the object into a dict
return_refund_methods_id_get200_response_dict = return_refund_methods_id_get200_response_instance.to_dict()
# create an instance of ReturnRefundMethodsIdGet200Response from a dict
return_refund_methods_id_get200_response_form_dict = return_refund_methods_id_get200_response.from_dict(return_refund_methods_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


