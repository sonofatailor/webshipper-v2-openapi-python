# BarcodeRangesGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BarcodeRangesGet200ResponseDataInner]**](BarcodeRangesGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.barcode_ranges_get200_response import BarcodeRangesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BarcodeRangesGet200Response from a JSON string
barcode_ranges_get200_response_instance = BarcodeRangesGet200Response.from_json(json)
# print the JSON string representation of the object
print BarcodeRangesGet200Response.to_json()

# convert the object into a dict
barcode_ranges_get200_response_dict = barcode_ranges_get200_response_instance.to_dict()
# create an instance of BarcodeRangesGet200Response from a dict
barcode_ranges_get200_response_form_dict = barcode_ranges_get200_response.from_dict(barcode_ranges_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


