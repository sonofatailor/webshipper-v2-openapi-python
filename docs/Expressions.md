# Expressions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | Is the actual WEL expression to be evaluated | [optional] 
**vat_percent** | **float** | VAT rate in percentage which must be added to the price. | [optional] 
**currency** | **str** | Currency of the price | [optional] 
**price** | **float** | The cost price displayed to the end user | [optional] 

## Example

```python
from openapi_client.models.expressions import Expressions

# TODO update the JSON string below
json = "{}"
# create an instance of Expressions from a JSON string
expressions_instance = Expressions.from_json(json)
# print the JSON string representation of the object
print Expressions.to_json()

# convert the object into a dict
expressions_dict = expressions_instance.to_dict()
# create an instance of Expressions from a dict
expressions_form_dict = expressions.from_dict(expressions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


