# HotKeysIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**HotKeysIdGet200ResponseData**](HotKeysIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**HotKeysIdGet200ResponseRelationships**](HotKeysIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.hot_keys_id_patch_request import HotKeysIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HotKeysIdPatchRequest from a JSON string
hot_keys_id_patch_request_instance = HotKeysIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print HotKeysIdPatchRequest.to_json()

# convert the object into a dict
hot_keys_id_patch_request_dict = hot_keys_id_patch_request_instance.to_dict()
# create an instance of HotKeysIdPatchRequest from a dict
hot_keys_id_patch_request_form_dict = hot_keys_id_patch_request.from_dict(hot_keys_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


