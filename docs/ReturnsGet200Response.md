# ReturnsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReturnsGet200ResponseDataInner]**](ReturnsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.returns_get200_response import ReturnsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsGet200Response from a JSON string
returns_get200_response_instance = ReturnsGet200Response.from_json(json)
# print the JSON string representation of the object
print ReturnsGet200Response.to_json()

# convert the object into a dict
returns_get200_response_dict = returns_get200_response_instance.to_dict()
# create an instance of ReturnsGet200Response from a dict
returns_get200_response_form_dict = returns_get200_response.from_dict(returns_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


