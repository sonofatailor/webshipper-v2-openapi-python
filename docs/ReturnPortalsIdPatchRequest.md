# ReturnPortalsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReturnPortalsIdGet200ResponseData**](ReturnPortalsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**ReturnPortalsIdGet200ResponseRelationships**](ReturnPortalsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.return_portals_id_patch_request import ReturnPortalsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnPortalsIdPatchRequest from a JSON string
return_portals_id_patch_request_instance = ReturnPortalsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ReturnPortalsIdPatchRequest.to_json()

# convert the object into a dict
return_portals_id_patch_request_dict = return_portals_id_patch_request_instance.to_dict()
# create an instance of ReturnPortalsIdPatchRequest from a dict
return_portals_id_patch_request_form_dict = return_portals_id_patch_request.from_dict(return_portals_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


