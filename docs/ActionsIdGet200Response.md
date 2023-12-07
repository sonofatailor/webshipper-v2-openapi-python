# ActionsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ActionsIdGet200ResponseData**](ActionsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**ActionsIdGet200ResponseRelationships**](ActionsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[ActionsIdGet200ResponseIncludedInner]**](ActionsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.actions_id_get200_response import ActionsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsIdGet200Response from a JSON string
actions_id_get200_response_instance = ActionsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print ActionsIdGet200Response.to_json()

# convert the object into a dict
actions_id_get200_response_dict = actions_id_get200_response_instance.to_dict()
# create an instance of ActionsIdGet200Response from a dict
actions_id_get200_response_form_dict = actions_id_get200_response.from_dict(actions_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


