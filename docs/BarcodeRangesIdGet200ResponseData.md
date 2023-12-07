# BarcodeRangesIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**BarcodeRanges**](BarcodeRanges.md) |  | [optional] 

## Example

```python
from openapi_client.models.barcode_ranges_id_get200_response_data import BarcodeRangesIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BarcodeRangesIdGet200ResponseData from a JSON string
barcode_ranges_id_get200_response_data_instance = BarcodeRangesIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print BarcodeRangesIdGet200ResponseData.to_json()

# convert the object into a dict
barcode_ranges_id_get200_response_data_dict = barcode_ranges_id_get200_response_data_instance.to_dict()
# create an instance of BarcodeRangesIdGet200ResponseData from a dict
barcode_ranges_id_get200_response_data_form_dict = barcode_ranges_id_get200_response_data.from_dict(barcode_ranges_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


