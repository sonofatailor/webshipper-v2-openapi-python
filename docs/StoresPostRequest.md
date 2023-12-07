# StoresPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**StoresPostRequestData**](StoresPostRequestData.md) |  | [optional] 
**relationships** | [**StoresIdGet200ResponseRelationships**](StoresIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.stores_post_request import StoresPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StoresPostRequest from a JSON string
stores_post_request_instance = StoresPostRequest.from_json(json)
# print the JSON string representation of the object
print StoresPostRequest.to_json()

# convert the object into a dict
stores_post_request_dict = stores_post_request_instance.to_dict()
# create an instance of StoresPostRequest from a dict
stores_post_request_form_dict = stores_post_request.from_dict(stores_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


