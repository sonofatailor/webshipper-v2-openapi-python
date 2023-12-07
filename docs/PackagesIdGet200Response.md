# PackagesIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PackagesIdGet200ResponseData**](PackagesIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**EdisIdGet200ResponseRelationships**](EdisIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[EdisIdGet200ResponseIncludedInner]**](EdisIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.packages_id_get200_response import PackagesIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PackagesIdGet200Response from a JSON string
packages_id_get200_response_instance = PackagesIdGet200Response.from_json(json)
# print the JSON string representation of the object
print PackagesIdGet200Response.to_json()

# convert the object into a dict
packages_id_get200_response_dict = packages_id_get200_response_instance.to_dict()
# create an instance of PackagesIdGet200Response from a dict
packages_id_get200_response_form_dict = packages_id_get200_response.from_dict(packages_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


