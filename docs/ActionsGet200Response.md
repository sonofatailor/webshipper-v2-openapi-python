# ActionsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ActionsGet200ResponseDataInner]**](ActionsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.actions_get200_response import ActionsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsGet200Response from a JSON string
actions_get200_response_instance = ActionsGet200Response.from_json(json)
# print the JSON string representation of the object
print ActionsGet200Response.to_json()

# convert the object into a dict
actions_get200_response_dict = actions_get200_response_instance.to_dict()
# create an instance of ActionsGet200Response from a dict
actions_get200_response_form_dict = actions_get200_response.from_dict(actions_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


