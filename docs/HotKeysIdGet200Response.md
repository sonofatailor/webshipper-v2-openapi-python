# HotKeysIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**HotKeysIdGet200ResponseData**](HotKeysIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**HotKeysIdGet200ResponseRelationships**](HotKeysIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[HotKeysIdGet200ResponseIncludedInner]**](HotKeysIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.hot_keys_id_get200_response import HotKeysIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of HotKeysIdGet200Response from a JSON string
hot_keys_id_get200_response_instance = HotKeysIdGet200Response.from_json(json)
# print the JSON string representation of the object
print HotKeysIdGet200Response.to_json()

# convert the object into a dict
hot_keys_id_get200_response_dict = hot_keys_id_get200_response_instance.to_dict()
# create an instance of HotKeysIdGet200Response from a dict
hot_keys_id_get200_response_form_dict = hot_keys_id_get200_response.from_dict(hot_keys_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


