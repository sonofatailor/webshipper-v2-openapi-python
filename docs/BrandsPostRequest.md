# BrandsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BrandsPostRequestData**](BrandsPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.brands_post_request import BrandsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BrandsPostRequest from a JSON string
brands_post_request_instance = BrandsPostRequest.from_json(json)
# print the JSON string representation of the object
print BrandsPostRequest.to_json()

# convert the object into a dict
brands_post_request_dict = brands_post_request_instance.to_dict()
# create an instance of BrandsPostRequest from a dict
brands_post_request_form_dict = brands_post_request.from_dict(brands_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


