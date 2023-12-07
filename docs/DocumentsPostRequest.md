# DocumentsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DocumentsPostRequestData**](DocumentsPostRequestData.md) |  | [optional] 
**relationships** | [**DocumentsIdGet200ResponseRelationships**](DocumentsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.documents_post_request import DocumentsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsPostRequest from a JSON string
documents_post_request_instance = DocumentsPostRequest.from_json(json)
# print the JSON string representation of the object
print DocumentsPostRequest.to_json()

# convert the object into a dict
documents_post_request_dict = documents_post_request_instance.to_dict()
# create an instance of DocumentsPostRequest from a dict
documents_post_request_form_dict = documents_post_request.from_dict(documents_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


