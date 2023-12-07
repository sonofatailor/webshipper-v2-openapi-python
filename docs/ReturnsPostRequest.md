# ReturnsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReturnsPostRequestData**](ReturnsPostRequestData.md) |  | [optional] 
**relationships** | [**ReturnsIdGet200ResponseRelationships**](ReturnsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.returns_post_request import ReturnsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsPostRequest from a JSON string
returns_post_request_instance = ReturnsPostRequest.from_json(json)
# print the JSON string representation of the object
print ReturnsPostRequest.to_json()

# convert the object into a dict
returns_post_request_dict = returns_post_request_instance.to_dict()
# create an instance of ReturnsPostRequest from a dict
returns_post_request_form_dict = returns_post_request.from_dict(returns_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


