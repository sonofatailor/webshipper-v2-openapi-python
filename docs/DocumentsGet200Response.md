# DocumentsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DocumentsGet200ResponseDataInner]**](DocumentsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.documents_get200_response import DocumentsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsGet200Response from a JSON string
documents_get200_response_instance = DocumentsGet200Response.from_json(json)
# print the JSON string representation of the object
print DocumentsGet200Response.to_json()

# convert the object into a dict
documents_get200_response_dict = documents_get200_response_instance.to_dict()
# create an instance of DocumentsGet200Response from a dict
documents_get200_response_form_dict = documents_get200_response.from_dict(documents_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


