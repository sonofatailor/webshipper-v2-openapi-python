# ReturnsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Returns**](Returns.md) |  | [optional] 

## Example

```python
from webshipperv2.models.returns_id_get200_response_data import ReturnsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsIdGet200ResponseData from a JSON string
returns_id_get200_response_data_instance = ReturnsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print ReturnsIdGet200ResponseData.to_json()

# convert the object into a dict
returns_id_get200_response_data_dict = returns_id_get200_response_data_instance.to_dict()
# create an instance of ReturnsIdGet200ResponseData from a dict
returns_id_get200_response_data_form_dict = returns_id_get200_response_data.from_dict(returns_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


