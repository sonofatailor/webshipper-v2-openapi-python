# UsersIdGet200ResponseIncludedInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**data** | [**UsersIdGet200ResponseIncludedInnerData**](UsersIdGet200ResponseIncludedInnerData.md) |  | [optional] 

## Example

```python
from webshipperv2.models.users_id_get200_response_included_inner import UsersIdGet200ResponseIncludedInner

# TODO update the JSON string below
json = "{}"
# create an instance of UsersIdGet200ResponseIncludedInner from a JSON string
users_id_get200_response_included_inner_instance = UsersIdGet200ResponseIncludedInner.from_json(json)
# print the JSON string representation of the object
print UsersIdGet200ResponseIncludedInner.to_json()

# convert the object into a dict
users_id_get200_response_included_inner_dict = users_id_get200_response_included_inner_instance.to_dict()
# create an instance of UsersIdGet200ResponseIncludedInner from a dict
users_id_get200_response_included_inner_form_dict = users_id_get200_response_included_inner.from_dict(users_id_get200_response_included_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


