# AttachmentsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AttachmentsPostRequestData**](AttachmentsPostRequestData.md) |  | [optional] 
**relationships** | [**AttachmentsIdGet200ResponseRelationships**](AttachmentsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.attachments_post_request import AttachmentsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentsPostRequest from a JSON string
attachments_post_request_instance = AttachmentsPostRequest.from_json(json)
# print the JSON string representation of the object
print AttachmentsPostRequest.to_json()

# convert the object into a dict
attachments_post_request_dict = attachments_post_request_instance.to_dict()
# create an instance of AttachmentsPostRequest from a dict
attachments_post_request_form_dict = attachments_post_request.from_dict(attachments_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


