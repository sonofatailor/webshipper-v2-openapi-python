# DocumentsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DocumentsIdGet200ResponseData**](DocumentsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**DocumentsIdGet200ResponseRelationships**](DocumentsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.documents_id_patch_request import DocumentsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsIdPatchRequest from a JSON string
documents_id_patch_request_instance = DocumentsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print DocumentsIdPatchRequest.to_json()

# convert the object into a dict
documents_id_patch_request_dict = documents_id_patch_request_instance.to_dict()
# create an instance of DocumentsIdPatchRequest from a dict
documents_id_patch_request_form_dict = documents_id_patch_request.from_dict(documents_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


