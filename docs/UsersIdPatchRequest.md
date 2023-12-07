# UsersIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UsersIdGet200ResponseData**](UsersIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**UsersIdGet200ResponseRelationships**](UsersIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.users_id_patch_request import UsersIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersIdPatchRequest from a JSON string
users_id_patch_request_instance = UsersIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print UsersIdPatchRequest.to_json()

# convert the object into a dict
users_id_patch_request_dict = users_id_patch_request_instance.to_dict()
# create an instance of UsersIdPatchRequest from a dict
users_id_patch_request_form_dict = users_id_patch_request.from_dict(users_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


