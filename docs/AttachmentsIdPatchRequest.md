# AttachmentsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AttachmentsIdGet200ResponseData**](AttachmentsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**AttachmentsIdGet200ResponseRelationships**](AttachmentsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.attachments_id_patch_request import AttachmentsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentsIdPatchRequest from a JSON string
attachments_id_patch_request_instance = AttachmentsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print AttachmentsIdPatchRequest.to_json()

# convert the object into a dict
attachments_id_patch_request_dict = attachments_id_patch_request_instance.to_dict()
# create an instance of AttachmentsIdPatchRequest from a dict
attachments_id_patch_request_form_dict = attachments_id_patch_request.from_dict(attachments_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


