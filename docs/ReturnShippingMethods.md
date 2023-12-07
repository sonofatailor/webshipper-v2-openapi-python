# ReturnShippingMethods


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from webshipperv2.models.return_shipping_methods import ReturnShippingMethods

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnShippingMethods from a JSON string
return_shipping_methods_instance = ReturnShippingMethods.from_json(json)
# print the JSON string representation of the object
print ReturnShippingMethods.to_json()

# convert the object into a dict
return_shipping_methods_dict = return_shipping_methods_instance.to_dict()
# create an instance of ReturnShippingMethods from a dict
return_shipping_methods_form_dict = return_shipping_methods.from_dict(return_shipping_methods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


