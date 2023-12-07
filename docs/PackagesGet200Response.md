# PackagesGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PackagesGet200ResponseDataInner]**](PackagesGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.packages_get200_response import PackagesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PackagesGet200Response from a JSON string
packages_get200_response_instance = PackagesGet200Response.from_json(json)
# print the JSON string representation of the object
print PackagesGet200Response.to_json()

# convert the object into a dict
packages_get200_response_dict = packages_get200_response_instance.to_dict()
# create an instance of PackagesGet200Response from a dict
packages_get200_response_form_dict = packages_get200_response.from_dict(packages_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


