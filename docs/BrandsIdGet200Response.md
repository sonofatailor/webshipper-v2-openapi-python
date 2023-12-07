# BrandsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BrandsIdGet200ResponseData**](BrandsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.brands_id_get200_response import BrandsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BrandsIdGet200Response from a JSON string
brands_id_get200_response_instance = BrandsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print BrandsIdGet200Response.to_json()

# convert the object into a dict
brands_id_get200_response_dict = brands_id_get200_response_instance.to_dict()
# create an instance of BrandsIdGet200Response from a dict
brands_id_get200_response_form_dict = brands_id_get200_response.from_dict(brands_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


