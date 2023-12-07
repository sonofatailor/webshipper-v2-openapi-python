# UserGroupsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserGroupsIdGet200ResponseData**](UserGroupsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_groups_id_get200_response import UserGroupsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupsIdGet200Response from a JSON string
user_groups_id_get200_response_instance = UserGroupsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print UserGroupsIdGet200Response.to_json()

# convert the object into a dict
user_groups_id_get200_response_dict = user_groups_id_get200_response_instance.to_dict()
# create an instance of UserGroupsIdGet200Response from a dict
user_groups_id_get200_response_form_dict = user_groups_id_get200_response.from_dict(user_groups_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


