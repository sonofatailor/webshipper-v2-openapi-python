# StoresPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Stores**](Stores.md) |  | [optional] 

## Example

```python
from openapi_client.models.stores_post_request_data import StoresPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of StoresPostRequestData from a JSON string
stores_post_request_data_instance = StoresPostRequestData.from_json(json)
# print the JSON string representation of the object
print StoresPostRequestData.to_json()

# convert the object into a dict
stores_post_request_data_dict = stores_post_request_data_instance.to_dict()
# create an instance of StoresPostRequestData from a dict
stores_post_request_data_form_dict = stores_post_request_data.from_dict(stores_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


