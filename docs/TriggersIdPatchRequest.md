# TriggersIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TriggersIdGet200ResponseData**](TriggersIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**ActionsIdGet200ResponseRelationships**](ActionsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.triggers_id_patch_request import TriggersIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TriggersIdPatchRequest from a JSON string
triggers_id_patch_request_instance = TriggersIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print TriggersIdPatchRequest.to_json()

# convert the object into a dict
triggers_id_patch_request_dict = triggers_id_patch_request_instance.to_dict()
# create an instance of TriggersIdPatchRequest from a dict
triggers_id_patch_request_form_dict = triggers_id_patch_request.from_dict(triggers_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


