# BarcodeRangesIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BarcodeRangesIdGet200ResponseData**](BarcodeRangesIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**BarcodeRangesIdGet200ResponseRelationships**](BarcodeRangesIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[BarcodeRangesIdGet200ResponseIncludedInner]**](BarcodeRangesIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.barcode_ranges_id_get200_response import BarcodeRangesIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BarcodeRangesIdGet200Response from a JSON string
barcode_ranges_id_get200_response_instance = BarcodeRangesIdGet200Response.from_json(json)
# print the JSON string representation of the object
print BarcodeRangesIdGet200Response.to_json()

# convert the object into a dict
barcode_ranges_id_get200_response_dict = barcode_ranges_id_get200_response_instance.to_dict()
# create an instance of BarcodeRangesIdGet200Response from a dict
barcode_ranges_id_get200_response_form_dict = barcode_ranges_id_get200_response.from_dict(barcode_ranges_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


