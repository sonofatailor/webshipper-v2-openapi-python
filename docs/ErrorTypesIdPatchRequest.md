# ErrorTypesIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ErrorTypesIdGet200ResponseData**](ErrorTypesIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.error_types_id_patch_request import ErrorTypesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorTypesIdPatchRequest from a JSON string
error_types_id_patch_request_instance = ErrorTypesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ErrorTypesIdPatchRequest.to_json()

# convert the object into a dict
error_types_id_patch_request_dict = error_types_id_patch_request_instance.to_dict()
# create an instance of ErrorTypesIdPatchRequest from a dict
error_types_id_patch_request_form_dict = error_types_id_patch_request.from_dict(error_types_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


