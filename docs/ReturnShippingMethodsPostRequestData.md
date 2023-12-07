# ReturnShippingMethodsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**ReturnShippingMethods**](ReturnShippingMethods.md) |  | [optional] 

## Example

```python
from webshipperv2.models.return_shipping_methods_post_request_data import ReturnShippingMethodsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnShippingMethodsPostRequestData from a JSON string
return_shipping_methods_post_request_data_instance = ReturnShippingMethodsPostRequestData.from_json(json)
# print the JSON string representation of the object
print ReturnShippingMethodsPostRequestData.to_json()

# convert the object into a dict
return_shipping_methods_post_request_data_dict = return_shipping_methods_post_request_data_instance.to_dict()
# create an instance of ReturnShippingMethodsPostRequestData from a dict
return_shipping_methods_post_request_data_form_dict = return_shipping_methods_post_request_data.from_dict(return_shipping_methods_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


