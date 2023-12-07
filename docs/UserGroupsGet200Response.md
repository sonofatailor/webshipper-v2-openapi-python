# UserGroupsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserGroupsGet200ResponseDataInner]**](UserGroupsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.user_groups_get200_response import UserGroupsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupsGet200Response from a JSON string
user_groups_get200_response_instance = UserGroupsGet200Response.from_json(json)
# print the JSON string representation of the object
print UserGroupsGet200Response.to_json()

# convert the object into a dict
user_groups_get200_response_dict = user_groups_get200_response_instance.to_dict()
# create an instance of UserGroupsGet200Response from a dict
user_groups_get200_response_form_dict = user_groups_get200_response.from_dict(user_groups_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


