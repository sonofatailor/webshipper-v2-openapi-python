# UserGroups


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the user group | [optional] 
**scopes** | **List[str]** | Array of scopes. Please see section 6 for more details regarding scopes. | [optional] 
**locked** | **bool** |  | [optional] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 

## Example

```python
from openapi_client.models.user_groups import UserGroups

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroups from a JSON string
user_groups_instance = UserGroups.from_json(json)
# print the JSON string representation of the object
print UserGroups.to_json()

# convert the object into a dict
user_groups_dict = user_groups_instance.to_dict()
# create an instance of UserGroups from a dict
user_groups_form_dict = user_groups.from_dict(user_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


