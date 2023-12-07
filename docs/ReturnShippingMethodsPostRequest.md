# ReturnShippingMethodsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReturnShippingMethodsPostRequestData**](ReturnShippingMethodsPostRequestData.md) |  | [optional] 
**relationships** | [**ReturnShippingMethodsIdGet200ResponseRelationships**](ReturnShippingMethodsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.return_shipping_methods_post_request import ReturnShippingMethodsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnShippingMethodsPostRequest from a JSON string
return_shipping_methods_post_request_instance = ReturnShippingMethodsPostRequest.from_json(json)
# print the JSON string representation of the object
print ReturnShippingMethodsPostRequest.to_json()

# convert the object into a dict
return_shipping_methods_post_request_dict = return_shipping_methods_post_request_instance.to_dict()
# create an instance of ReturnShippingMethodsPostRequest from a dict
return_shipping_methods_post_request_form_dict = return_shipping_methods_post_request.from_dict(return_shipping_methods_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


