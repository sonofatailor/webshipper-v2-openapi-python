# ReturnRefundMethodsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**ReturnRefundMethods**](ReturnRefundMethods.md) |  | [optional] 

## Example

```python
from webshipperv2.models.return_refund_methods_id_get200_response_data import ReturnRefundMethodsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnRefundMethodsIdGet200ResponseData from a JSON string
return_refund_methods_id_get200_response_data_instance = ReturnRefundMethodsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print ReturnRefundMethodsIdGet200ResponseData.to_json()

# convert the object into a dict
return_refund_methods_id_get200_response_data_dict = return_refund_methods_id_get200_response_data_instance.to_dict()
# create an instance of ReturnRefundMethodsIdGet200ResponseData from a dict
return_refund_methods_id_get200_response_data_form_dict = return_refund_methods_id_get200_response_data.from_dict(return_refund_methods_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


