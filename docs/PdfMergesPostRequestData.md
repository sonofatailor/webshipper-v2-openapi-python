# PdfMergesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**PdfMerges**](PdfMerges.md) |  | [optional] 

## Example

```python
from openapi_client.models.pdf_merges_post_request_data import PdfMergesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of PdfMergesPostRequestData from a JSON string
pdf_merges_post_request_data_instance = PdfMergesPostRequestData.from_json(json)
# print the JSON string representation of the object
print PdfMergesPostRequestData.to_json()

# convert the object into a dict
pdf_merges_post_request_data_dict = pdf_merges_post_request_data_instance.to_dict()
# create an instance of PdfMergesPostRequestData from a dict
pdf_merges_post_request_data_form_dict = pdf_merges_post_request_data.from_dict(pdf_merges_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


