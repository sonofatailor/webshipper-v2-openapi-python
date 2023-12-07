# ReturnShippingMethodsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**ReturnShippingMethods**](ReturnShippingMethods.md) |  | [optional] 

## Example

```python
from openapi_client.models.return_shipping_methods_id_get200_response_data import ReturnShippingMethodsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnShippingMethodsIdGet200ResponseData from a JSON string
return_shipping_methods_id_get200_response_data_instance = ReturnShippingMethodsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print ReturnShippingMethodsIdGet200ResponseData.to_json()

# convert the object into a dict
return_shipping_methods_id_get200_response_data_dict = return_shipping_methods_id_get200_response_data_instance.to_dict()
# create an instance of ReturnShippingMethodsIdGet200ResponseData from a dict
return_shipping_methods_id_get200_response_data_form_dict = return_shipping_methods_id_get200_response_data.from_dict(return_shipping_methods_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


