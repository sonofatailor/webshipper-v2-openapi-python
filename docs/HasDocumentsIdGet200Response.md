# HasDocumentsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**HasDocumentsIdGet200ResponseData**](HasDocumentsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.has_documents_id_get200_response import HasDocumentsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of HasDocumentsIdGet200Response from a JSON string
has_documents_id_get200_response_instance = HasDocumentsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print HasDocumentsIdGet200Response.to_json()

# convert the object into a dict
has_documents_id_get200_response_dict = has_documents_id_get200_response_instance.to_dict()
# create an instance of HasDocumentsIdGet200Response from a dict
has_documents_id_get200_response_form_dict = has_documents_id_get200_response.from_dict(has_documents_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


