# ReturnsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Returns**](Returns.md) |  | [optional] 

## Example

```python
from openapi_client.models.returns_post_request_data import ReturnsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsPostRequestData from a JSON string
returns_post_request_data_instance = ReturnsPostRequestData.from_json(json)
# print the JSON string representation of the object
print ReturnsPostRequestData.to_json()

# convert the object into a dict
returns_post_request_data_dict = returns_post_request_data_instance.to_dict()
# create an instance of ReturnsPostRequestData from a dict
returns_post_request_data_form_dict = returns_post_request_data.from_dict(returns_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


