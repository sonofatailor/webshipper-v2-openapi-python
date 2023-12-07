# UserGroupsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**UserGroups**](UserGroups.md) |  | [optional] 

## Example

```python
from webshipperv2.models.user_groups_id_get200_response_data import UserGroupsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupsIdGet200ResponseData from a JSON string
user_groups_id_get200_response_data_instance = UserGroupsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print UserGroupsIdGet200ResponseData.to_json()

# convert the object into a dict
user_groups_id_get200_response_data_dict = user_groups_id_get200_response_data_instance.to_dict()
# create an instance of UserGroupsIdGet200ResponseData from a dict
user_groups_id_get200_response_data_form_dict = user_groups_id_get200_response_data.from_dict(user_groups_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


