# LocalAttrsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**LocalAttrs**](LocalAttrs.md) |  | [optional] 

## Example

```python
from openapi_client.models.local_attrs_id_get200_response_data import LocalAttrsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of LocalAttrsIdGet200ResponseData from a JSON string
local_attrs_id_get200_response_data_instance = LocalAttrsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print LocalAttrsIdGet200ResponseData.to_json()

# convert the object into a dict
local_attrs_id_get200_response_data_dict = local_attrs_id_get200_response_data_instance.to_dict()
# create an instance of LocalAttrsIdGet200ResponseData from a dict
local_attrs_id_get200_response_data_form_dict = local_attrs_id_get200_response_data.from_dict(local_attrs_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


