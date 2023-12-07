# StoresIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**StoresIdGet200ResponseData**](StoresIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**StoresIdGet200ResponseRelationships**](StoresIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.stores_id_patch_request import StoresIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StoresIdPatchRequest from a JSON string
stores_id_patch_request_instance = StoresIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print StoresIdPatchRequest.to_json()

# convert the object into a dict
stores_id_patch_request_dict = stores_id_patch_request_instance.to_dict()
# create an instance of StoresIdPatchRequest from a dict
stores_id_patch_request_form_dict = stores_id_patch_request.from_dict(stores_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


