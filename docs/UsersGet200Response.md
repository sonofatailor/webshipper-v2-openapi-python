# UsersGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UsersGet200ResponseDataInner]**](UsersGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.users_get200_response import UsersGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsersGet200Response from a JSON string
users_get200_response_instance = UsersGet200Response.from_json(json)
# print the JSON string representation of the object
print UsersGet200Response.to_json()

# convert the object into a dict
users_get200_response_dict = users_get200_response_instance.to_dict()
# create an instance of UsersGet200Response from a dict
users_get200_response_form_dict = users_get200_response.from_dict(users_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


