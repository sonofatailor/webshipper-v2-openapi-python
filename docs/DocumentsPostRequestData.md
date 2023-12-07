# DocumentsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Documents**](Documents.md) |  | [optional] 

## Example

```python
from webshipperv2.models.documents_post_request_data import DocumentsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsPostRequestData from a JSON string
documents_post_request_data_instance = DocumentsPostRequestData.from_json(json)
# print the JSON string representation of the object
print DocumentsPostRequestData.to_json()

# convert the object into a dict
documents_post_request_data_dict = documents_post_request_data_instance.to_dict()
# create an instance of DocumentsPostRequestData from a dict
documents_post_request_data_form_dict = documents_post_request_data.from_dict(documents_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


