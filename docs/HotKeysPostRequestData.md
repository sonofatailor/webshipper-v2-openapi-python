# HotKeysPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**HotKeys**](HotKeys.md) |  | [optional] 

## Example

```python
from webshipperv2.models.hot_keys_post_request_data import HotKeysPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of HotKeysPostRequestData from a JSON string
hot_keys_post_request_data_instance = HotKeysPostRequestData.from_json(json)
# print the JSON string representation of the object
print HotKeysPostRequestData.to_json()

# convert the object into a dict
hot_keys_post_request_data_dict = hot_keys_post_request_data_instance.to_dict()
# create an instance of HotKeysPostRequestData from a dict
hot_keys_post_request_data_form_dict = hot_keys_post_request_data.from_dict(hot_keys_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


