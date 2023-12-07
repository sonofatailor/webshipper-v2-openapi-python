# UsersIdGet200ResponseIncludedInnerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the user group | [optional] 
**scopes** | **List[str]** | Array of scopes. Please see section 6 for more details regarding scopes. | [optional] 
**locked** | **bool** |  | [optional] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**uuid** | **str** | Unique ID of the printer client | [optional] 
**approved** | **bool** | DEPRECATED | [optional] 
**alias** | **str** | Defaults to the host name of the machine running the client  | [optional] 
**is_online** | **bool** | Shows if the printer client is online | [optional] 
**last_connected** | **str** | Shows when the printer client was last connected | [optional] 
**prevent_multiple_shipments** | **bool** |  | [optional] 

## Example

```python
from webshipperv2.models.users_id_get200_response_included_inner_data import UsersIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of UsersIdGet200ResponseIncludedInnerData from a JSON string
users_id_get200_response_included_inner_data_instance = UsersIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print UsersIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
users_id_get200_response_included_inner_data_dict = users_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of UsersIdGet200ResponseIncludedInnerData from a dict
users_id_get200_response_included_inner_data_form_dict = users_id_get200_response_included_inner_data.from_dict(users_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


