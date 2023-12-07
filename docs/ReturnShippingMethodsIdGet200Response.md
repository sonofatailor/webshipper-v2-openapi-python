# ReturnShippingMethodsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReturnShippingMethodsIdGet200ResponseData**](ReturnShippingMethodsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**ReturnShippingMethodsIdGet200ResponseRelationships**](ReturnShippingMethodsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[ReturnShippingMethodsIdGet200ResponseIncludedInner]**](ReturnShippingMethodsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.return_shipping_methods_id_get200_response import ReturnShippingMethodsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnShippingMethodsIdGet200Response from a JSON string
return_shipping_methods_id_get200_response_instance = ReturnShippingMethodsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print ReturnShippingMethodsIdGet200Response.to_json()

# convert the object into a dict
return_shipping_methods_id_get200_response_dict = return_shipping_methods_id_get200_response_instance.to_dict()
# create an instance of ReturnShippingMethodsIdGet200Response from a dict
return_shipping_methods_id_get200_response_form_dict = return_shipping_methods_id_get200_response.from_dict(return_shipping_methods_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


