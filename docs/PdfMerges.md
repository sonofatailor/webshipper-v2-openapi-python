# PdfMerges


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_labels** | **bool** | Whether to include labels or not | [optional] 
**include_docs** | **bool** | Whether to include docs or not&#39;  | [optional] 
**include_slips** | **bool** | Whether to include slips or not | [optional] 
**force_a4** | **bool** | Whether to use A4 paper size not | [optional] 
**shipment_ids** | **List[str]** | A list of shipment ids to include in the merged pdf | [optional] 
**order_ids** | **List[str]** | A list of order ids to include in the merged pdf | [optional] 
**url** | **str** |  | [optional] 
**failed** | **bool** |  | [optional] 

## Example

```python
from webshipperv2.models.pdf_merges import PdfMerges

# TODO update the JSON string below
json = "{}"
# create an instance of PdfMerges from a JSON string
pdf_merges_instance = PdfMerges.from_json(json)
# print the JSON string representation of the object
print PdfMerges.to_json()

# convert the object into a dict
pdf_merges_dict = pdf_merges_instance.to_dict()
# create an instance of PdfMerges from a dict
pdf_merges_form_dict = pdf_merges.from_dict(pdf_merges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


