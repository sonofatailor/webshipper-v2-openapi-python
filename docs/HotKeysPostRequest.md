# HotKeysPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**HotKeysPostRequestData**](HotKeysPostRequestData.md) |  | [optional] 
**relationships** | [**HotKeysIdGet200ResponseRelationships**](HotKeysIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.hot_keys_post_request import HotKeysPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HotKeysPostRequest from a JSON string
hot_keys_post_request_instance = HotKeysPostRequest.from_json(json)
# print the JSON string representation of the object
print HotKeysPostRequest.to_json()

# convert the object into a dict
hot_keys_post_request_dict = hot_keys_post_request_instance.to_dict()
# create an instance of HotKeysPostRequest from a dict
hot_keys_post_request_form_dict = hot_keys_post_request.from_dict(hot_keys_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


