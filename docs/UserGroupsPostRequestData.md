# UserGroupsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**UserGroups**](UserGroups.md) |  | [optional] 

## Example

```python
from webshipperv2.models.user_groups_post_request_data import UserGroupsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupsPostRequestData from a JSON string
user_groups_post_request_data_instance = UserGroupsPostRequestData.from_json(json)
# print the JSON string representation of the object
print UserGroupsPostRequestData.to_json()

# convert the object into a dict
user_groups_post_request_data_dict = user_groups_post_request_data_instance.to_dict()
# create an instance of UserGroupsPostRequestData from a dict
user_groups_post_request_data_form_dict = user_groups_post_request_data.from_dict(user_groups_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


