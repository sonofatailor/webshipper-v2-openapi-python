# UsersPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UsersPostRequestData**](UsersPostRequestData.md) |  | [optional] 
**relationships** | [**UsersIdGet200ResponseRelationships**](UsersIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.users_post_request import UsersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersPostRequest from a JSON string
users_post_request_instance = UsersPostRequest.from_json(json)
# print the JSON string representation of the object
print UsersPostRequest.to_json()

# convert the object into a dict
users_post_request_dict = users_post_request_instance.to_dict()
# create an instance of UsersPostRequest from a dict
users_post_request_form_dict = users_post_request.from_dict(users_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


