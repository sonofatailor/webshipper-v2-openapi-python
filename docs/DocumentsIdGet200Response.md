# DocumentsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DocumentsIdGet200ResponseData**](DocumentsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**DocumentsIdGet200ResponseRelationships**](DocumentsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[DocumentsIdGet200ResponseIncludedInner]**](DocumentsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.documents_id_get200_response import DocumentsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsIdGet200Response from a JSON string
documents_id_get200_response_instance = DocumentsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print DocumentsIdGet200Response.to_json()

# convert the object into a dict
documents_id_get200_response_dict = documents_id_get200_response_instance.to_dict()
# create an instance of DocumentsIdGet200Response from a dict
documents_id_get200_response_form_dict = documents_id_get200_response.from_dict(documents_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


