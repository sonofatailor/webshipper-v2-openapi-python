# PdfMergesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PdfMergesPostRequestData**](PdfMergesPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.pdf_merges_post_request import PdfMergesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PdfMergesPostRequest from a JSON string
pdf_merges_post_request_instance = PdfMergesPostRequest.from_json(json)
# print the JSON string representation of the object
print PdfMergesPostRequest.to_json()

# convert the object into a dict
pdf_merges_post_request_dict = pdf_merges_post_request_instance.to_dict()
# create an instance of PdfMergesPostRequest from a dict
pdf_merges_post_request_form_dict = pdf_merges_post_request.from_dict(pdf_merges_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


