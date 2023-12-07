# BarcodeRangesIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BarcodeRangesIdGet200ResponseData**](BarcodeRangesIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**BarcodeRangesIdGet200ResponseRelationships**](BarcodeRangesIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.barcode_ranges_id_patch_request import BarcodeRangesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BarcodeRangesIdPatchRequest from a JSON string
barcode_ranges_id_patch_request_instance = BarcodeRangesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print BarcodeRangesIdPatchRequest.to_json()

# convert the object into a dict
barcode_ranges_id_patch_request_dict = barcode_ranges_id_patch_request_instance.to_dict()
# create an instance of BarcodeRangesIdPatchRequest from a dict
barcode_ranges_id_patch_request_form_dict = barcode_ranges_id_patch_request.from_dict(barcode_ranges_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


