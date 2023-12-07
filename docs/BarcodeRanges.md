# BarcodeRanges


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode_type** | **str** | String like DPD or SSCC | [optional] 
**serial_from** | **int** | The first barcode in the range | [optional] 
**serial_to** | **int** | The last barcode in the range | [optional] 
**current_serial** | **int** | The last used (highest) barcode serial | [optional] [readonly] 
**usage_status** | **int** |  | [optional] 
**replaces_id** | **str** |  | [optional] 

## Example

```python
from webshipperv2.models.barcode_ranges import BarcodeRanges

# TODO update the JSON string below
json = "{}"
# create an instance of BarcodeRanges from a JSON string
barcode_ranges_instance = BarcodeRanges.from_json(json)
# print the JSON string representation of the object
print BarcodeRanges.to_json()

# convert the object into a dict
barcode_ranges_dict = barcode_ranges_instance.to_dict()
# create an instance of BarcodeRanges from a dict
barcode_ranges_form_dict = barcode_ranges.from_dict(barcode_ranges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


