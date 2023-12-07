# BrandsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BrandsGet200ResponseDataInner]**](BrandsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.brands_get200_response import BrandsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BrandsGet200Response from a JSON string
brands_get200_response_instance = BrandsGet200Response.from_json(json)
# print the JSON string representation of the object
print BrandsGet200Response.to_json()

# convert the object into a dict
brands_get200_response_dict = brands_get200_response_instance.to_dict()
# create an instance of BrandsGet200Response from a dict
brands_get200_response_form_dict = brands_get200_response.from_dict(brands_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


