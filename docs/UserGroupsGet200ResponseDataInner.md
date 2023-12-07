# UserGroupsGet200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserGroups**](UserGroups.md) |  | [optional] 

## Example

```python
from webshipperv2.models.user_groups_get200_response_data_inner import UserGroupsGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupsGet200ResponseDataInner from a JSON string
user_groups_get200_response_data_inner_instance = UserGroupsGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print UserGroupsGet200ResponseDataInner.to_json()

# convert the object into a dict
user_groups_get200_response_data_inner_dict = user_groups_get200_response_data_inner_instance.to_dict()
# create an instance of UserGroupsGet200ResponseDataInner from a dict
user_groups_get200_response_data_inner_form_dict = user_groups_get200_response_data_inner.from_dict(user_groups_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


