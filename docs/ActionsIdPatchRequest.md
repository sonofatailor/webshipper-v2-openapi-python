# ActionsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ActionsIdGet200ResponseData**](ActionsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**ActionsIdGet200ResponseRelationships**](ActionsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.actions_id_patch_request import ActionsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsIdPatchRequest from a JSON string
actions_id_patch_request_instance = ActionsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ActionsIdPatchRequest.to_json()

# convert the object into a dict
actions_id_patch_request_dict = actions_id_patch_request_instance.to_dict()
# create an instance of ActionsIdPatchRequest from a dict
actions_id_patch_request_form_dict = actions_id_patch_request.from_dict(actions_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


