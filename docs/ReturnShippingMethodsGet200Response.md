# ReturnShippingMethodsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReturnShippingMethodsGet200ResponseDataInner]**](ReturnShippingMethodsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.return_shipping_methods_get200_response import ReturnShippingMethodsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnShippingMethodsGet200Response from a JSON string
return_shipping_methods_get200_response_instance = ReturnShippingMethodsGet200Response.from_json(json)
# print the JSON string representation of the object
print ReturnShippingMethodsGet200Response.to_json()

# convert the object into a dict
return_shipping_methods_get200_response_dict = return_shipping_methods_get200_response_instance.to_dict()
# create an instance of ReturnShippingMethodsGet200Response from a dict
return_shipping_methods_get200_response_form_dict = return_shipping_methods_get200_response.from_dict(return_shipping_methods_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


