# UserGroupsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserGroupsIdGet200ResponseData**](UserGroupsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.user_groups_id_patch_request import UserGroupsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupsIdPatchRequest from a JSON string
user_groups_id_patch_request_instance = UserGroupsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print UserGroupsIdPatchRequest.to_json()

# convert the object into a dict
user_groups_id_patch_request_dict = user_groups_id_patch_request_instance.to_dict()
# create an instance of UserGroupsIdPatchRequest from a dict
user_groups_id_patch_request_form_dict = user_groups_id_patch_request.from_dict(user_groups_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


