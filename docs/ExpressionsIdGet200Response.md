# ExpressionsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ExpressionsIdGet200ResponseData**](ExpressionsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.expressions_id_get200_response import ExpressionsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExpressionsIdGet200Response from a JSON string
expressions_id_get200_response_instance = ExpressionsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print ExpressionsIdGet200Response.to_json()

# convert the object into a dict
expressions_id_get200_response_dict = expressions_id_get200_response_instance.to_dict()
# create an instance of ExpressionsIdGet200Response from a dict
expressions_id_get200_response_form_dict = expressions_id_get200_response.from_dict(expressions_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


