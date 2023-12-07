# DocumentsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Documents**](Documents.md) |  | [optional] 

## Example

```python
from openapi_client.models.documents_id_get200_response_data import DocumentsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsIdGet200ResponseData from a JSON string
documents_id_get200_response_data_instance = DocumentsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print DocumentsIdGet200ResponseData.to_json()

# convert the object into a dict
documents_id_get200_response_data_dict = documents_id_get200_response_data_instance.to_dict()
# create an instance of DocumentsIdGet200ResponseData from a dict
documents_id_get200_response_data_form_dict = documents_id_get200_response_data.from_dict(documents_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


