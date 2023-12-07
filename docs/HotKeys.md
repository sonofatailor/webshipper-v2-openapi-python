# HotKeys


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hot_key** | **str** | Key combination of the hotkey | [optional] 
**path** | **str** | Path the hotkey is assigned to | [optional] 
**favourite_page_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from webshipperv2.models.hot_keys import HotKeys

# TODO update the JSON string below
json = "{}"
# create an instance of HotKeys from a JSON string
hot_keys_instance = HotKeys.from_json(json)
# print the JSON string representation of the object
print HotKeys.to_json()

# convert the object into a dict
hot_keys_dict = hot_keys_instance.to_dict()
# create an instance of HotKeys from a dict
hot_keys_form_dict = hot_keys.from_dict(hot_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


