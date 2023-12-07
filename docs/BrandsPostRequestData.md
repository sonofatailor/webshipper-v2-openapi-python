# BrandsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Brands**](Brands.md) |  | [optional] 

## Example

```python
from webshipperv2.models.brands_post_request_data import BrandsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of BrandsPostRequestData from a JSON string
brands_post_request_data_instance = BrandsPostRequestData.from_json(json)
# print the JSON string representation of the object
print BrandsPostRequestData.to_json()

# convert the object into a dict
brands_post_request_data_dict = brands_post_request_data_instance.to_dict()
# create an instance of BrandsPostRequestData from a dict
brands_post_request_data_form_dict = brands_post_request_data.from_dict(brands_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


