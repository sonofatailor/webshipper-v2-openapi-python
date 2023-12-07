# ExpressionsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ExpressionsGet200ResponseDataInner]**](ExpressionsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.expressions_get200_response import ExpressionsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExpressionsGet200Response from a JSON string
expressions_get200_response_instance = ExpressionsGet200Response.from_json(json)
# print the JSON string representation of the object
print ExpressionsGet200Response.to_json()

# convert the object into a dict
expressions_get200_response_dict = expressions_get200_response_instance.to_dict()
# create an instance of ExpressionsGet200Response from a dict
expressions_get200_response_form_dict = expressions_get200_response.from_dict(expressions_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


