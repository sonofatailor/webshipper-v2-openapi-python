# BarcodeRangesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BarcodeRangesPostRequestData**](BarcodeRangesPostRequestData.md) |  | [optional] 
**relationships** | [**BarcodeRangesIdGet200ResponseRelationships**](BarcodeRangesIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.barcode_ranges_post_request import BarcodeRangesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BarcodeRangesPostRequest from a JSON string
barcode_ranges_post_request_instance = BarcodeRangesPostRequest.from_json(json)
# print the JSON string representation of the object
print BarcodeRangesPostRequest.to_json()

# convert the object into a dict
barcode_ranges_post_request_dict = barcode_ranges_post_request_instance.to_dict()
# create an instance of BarcodeRangesPostRequest from a dict
barcode_ranges_post_request_form_dict = barcode_ranges_post_request.from_dict(barcode_ranges_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


