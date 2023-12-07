# UsersIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_group** | [**UsersIdGet200ResponseRelationshipsUserGroup**](UsersIdGet200ResponseRelationshipsUserGroup.md) |  | [optional] 
**printer_client** | [**OrdersIdGet200ResponseRelationshipsPrinterClient**](OrdersIdGet200ResponseRelationshipsPrinterClient.md) |  | [optional] 

## Example

```python
from openapi_client.models.users_id_get200_response_relationships import UsersIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UsersIdGet200ResponseRelationships from a JSON string
users_id_get200_response_relationships_instance = UsersIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print UsersIdGet200ResponseRelationships.to_json()

# convert the object into a dict
users_id_get200_response_relationships_dict = users_id_get200_response_relationships_instance.to_dict()
# create an instance of UsersIdGet200ResponseRelationships from a dict
users_id_get200_response_relationships_form_dict = users_id_get200_response_relationships.from_dict(users_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


