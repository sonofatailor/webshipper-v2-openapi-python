# HasDocumentsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**HasDocumentsPostRequestData**](HasDocumentsPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.has_documents_post_request import HasDocumentsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HasDocumentsPostRequest from a JSON string
has_documents_post_request_instance = HasDocumentsPostRequest.from_json(json)
# print the JSON string representation of the object
print HasDocumentsPostRequest.to_json()

# convert the object into a dict
has_documents_post_request_dict = has_documents_post_request_instance.to_dict()
# create an instance of HasDocumentsPostRequest from a dict
has_documents_post_request_form_dict = has_documents_post_request.from_dict(has_documents_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


