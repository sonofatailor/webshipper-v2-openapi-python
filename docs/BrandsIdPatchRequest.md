# BrandsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BrandsIdGet200ResponseData**](BrandsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.brands_id_patch_request import BrandsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BrandsIdPatchRequest from a JSON string
brands_id_patch_request_instance = BrandsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print BrandsIdPatchRequest.to_json()

# convert the object into a dict
brands_id_patch_request_dict = brands_id_patch_request_instance.to_dict()
# create an instance of BrandsIdPatchRequest from a dict
brands_id_patch_request_form_dict = brands_id_patch_request.from_dict(brands_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


