# HotKeysIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**HotKeys**](HotKeys.md) |  | [optional] 

## Example

```python
from webshipperv2.models.hot_keys_id_get200_response_data import HotKeysIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of HotKeysIdGet200ResponseData from a JSON string
hot_keys_id_get200_response_data_instance = HotKeysIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print HotKeysIdGet200ResponseData.to_json()

# convert the object into a dict
hot_keys_id_get200_response_data_dict = hot_keys_id_get200_response_data_instance.to_dict()
# create an instance of HotKeysIdGet200ResponseData from a dict
hot_keys_id_get200_response_data_form_dict = hot_keys_id_get200_response_data.from_dict(hot_keys_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


