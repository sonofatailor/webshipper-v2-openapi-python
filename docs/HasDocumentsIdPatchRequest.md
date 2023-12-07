# HasDocumentsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**HasDocumentsIdGet200ResponseData**](HasDocumentsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.has_documents_id_patch_request import HasDocumentsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HasDocumentsIdPatchRequest from a JSON string
has_documents_id_patch_request_instance = HasDocumentsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print HasDocumentsIdPatchRequest.to_json()

# convert the object into a dict
has_documents_id_patch_request_dict = has_documents_id_patch_request_instance.to_dict()
# create an instance of HasDocumentsIdPatchRequest from a dict
has_documents_id_patch_request_form_dict = has_documents_id_patch_request.from_dict(has_documents_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


