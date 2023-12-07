# ErrorTypesGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ErrorTypesGet200ResponseDataInner]**](ErrorTypesGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.error_types_get200_response import ErrorTypesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorTypesGet200Response from a JSON string
error_types_get200_response_instance = ErrorTypesGet200Response.from_json(json)
# print the JSON string representation of the object
print ErrorTypesGet200Response.to_json()

# convert the object into a dict
error_types_get200_response_dict = error_types_get200_response_instance.to_dict()
# create an instance of ErrorTypesGet200Response from a dict
error_types_get200_response_form_dict = error_types_get200_response.from_dict(error_types_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


