# UsersPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Users**](Users.md) |  | [optional] 

## Example

```python
from openapi_client.models.users_post_request_data import UsersPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of UsersPostRequestData from a JSON string
users_post_request_data_instance = UsersPostRequestData.from_json(json)
# print the JSON string representation of the object
print UsersPostRequestData.to_json()

# convert the object into a dict
users_post_request_data_dict = users_post_request_data_instance.to_dict()
# create an instance of UsersPostRequestData from a dict
users_post_request_data_form_dict = users_post_request_data.from_dict(users_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


