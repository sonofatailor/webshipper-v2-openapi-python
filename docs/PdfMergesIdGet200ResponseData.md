# PdfMergesIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**PdfMerges**](PdfMerges.md) |  | [optional] 

## Example

```python
from webshipperv2.models.pdf_merges_id_get200_response_data import PdfMergesIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PdfMergesIdGet200ResponseData from a JSON string
pdf_merges_id_get200_response_data_instance = PdfMergesIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print PdfMergesIdGet200ResponseData.to_json()

# convert the object into a dict
pdf_merges_id_get200_response_data_dict = pdf_merges_id_get200_response_data_instance.to_dict()
# create an instance of PdfMergesIdGet200ResponseData from a dict
pdf_merges_id_get200_response_data_form_dict = pdf_merges_id_get200_response_data.from_dict(pdf_merges_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


