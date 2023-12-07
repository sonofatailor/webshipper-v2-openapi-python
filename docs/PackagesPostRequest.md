# PackagesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PackagesPostRequestData**](PackagesPostRequestData.md) |  | [optional] 
**relationships** | [**EdisIdGet200ResponseRelationships**](EdisIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.packages_post_request import PackagesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PackagesPostRequest from a JSON string
packages_post_request_instance = PackagesPostRequest.from_json(json)
# print the JSON string representation of the object
print PackagesPostRequest.to_json()

# convert the object into a dict
packages_post_request_dict = packages_post_request_instance.to_dict()
# create an instance of PackagesPostRequest from a dict
packages_post_request_form_dict = packages_post_request.from_dict(packages_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


