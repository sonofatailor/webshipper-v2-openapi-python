# HotKeysGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HotKeysGet200ResponseDataInner]**](HotKeysGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.hot_keys_get200_response import HotKeysGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of HotKeysGet200Response from a JSON string
hot_keys_get200_response_instance = HotKeysGet200Response.from_json(json)
# print the JSON string representation of the object
print HotKeysGet200Response.to_json()

# convert the object into a dict
hot_keys_get200_response_dict = hot_keys_get200_response_instance.to_dict()
# create an instance of HotKeysGet200Response from a dict
hot_keys_get200_response_form_dict = hot_keys_get200_response.from_dict(hot_keys_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


