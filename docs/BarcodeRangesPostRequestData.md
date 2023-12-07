# BarcodeRangesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**BarcodeRanges**](BarcodeRanges.md) |  | [optional] 

## Example

```python
from openapi_client.models.barcode_ranges_post_request_data import BarcodeRangesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of BarcodeRangesPostRequestData from a JSON string
barcode_ranges_post_request_data_instance = BarcodeRangesPostRequestData.from_json(json)
# print the JSON string representation of the object
print BarcodeRangesPostRequestData.to_json()

# convert the object into a dict
barcode_ranges_post_request_data_dict = barcode_ranges_post_request_data_instance.to_dict()
# create an instance of BarcodeRangesPostRequestData from a dict
barcode_ranges_post_request_data_form_dict = barcode_ranges_post_request_data.from_dict(barcode_ranges_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


