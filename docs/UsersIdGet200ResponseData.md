# UsersIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Users**](Users.md) |  | [optional] 

## Example

```python
from webshipperv2.models.users_id_get200_response_data import UsersIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UsersIdGet200ResponseData from a JSON string
users_id_get200_response_data_instance = UsersIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print UsersIdGet200ResponseData.to_json()

# convert the object into a dict
users_id_get200_response_data_dict = users_id_get200_response_data_instance.to_dict()
# create an instance of UsersIdGet200ResponseData from a dict
users_id_get200_response_data_form_dict = users_id_get200_response_data.from_dict(users_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


