# BrandsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Brands**](Brands.md) |  | [optional] 

## Example

```python
from webshipperv2.models.brands_id_get200_response_data import BrandsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BrandsIdGet200ResponseData from a JSON string
brands_id_get200_response_data_instance = BrandsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print BrandsIdGet200ResponseData.to_json()

# convert the object into a dict
brands_id_get200_response_data_dict = brands_id_get200_response_data_instance.to_dict()
# create an instance of BrandsIdGet200ResponseData from a dict
brands_id_get200_response_data_form_dict = brands_id_get200_response_data.from_dict(brands_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


