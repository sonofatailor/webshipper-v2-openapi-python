# UserGroupsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserGroupsPostRequestData**](UserGroupsPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.user_groups_post_request import UserGroupsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupsPostRequest from a JSON string
user_groups_post_request_instance = UserGroupsPostRequest.from_json(json)
# print the JSON string representation of the object
print UserGroupsPostRequest.to_json()

# convert the object into a dict
user_groups_post_request_dict = user_groups_post_request_instance.to_dict()
# create an instance of UserGroupsPostRequest from a dict
user_groups_post_request_form_dict = user_groups_post_request.from_dict(user_groups_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


