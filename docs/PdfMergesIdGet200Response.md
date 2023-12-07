# PdfMergesIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PdfMergesIdGet200ResponseData**](PdfMergesIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.pdf_merges_id_get200_response import PdfMergesIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PdfMergesIdGet200Response from a JSON string
pdf_merges_id_get200_response_instance = PdfMergesIdGet200Response.from_json(json)
# print the JSON string representation of the object
print PdfMergesIdGet200Response.to_json()

# convert the object into a dict
pdf_merges_id_get200_response_dict = pdf_merges_id_get200_response_instance.to_dict()
# create an instance of PdfMergesIdGet200Response from a dict
pdf_merges_id_get200_response_form_dict = pdf_merges_id_get200_response.from_dict(pdf_merges_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


