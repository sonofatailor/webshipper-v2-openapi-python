# StoresIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Stores**](Stores.md) |  | [optional] 

## Example

```python
from webshipperv2.models.stores_id_get200_response_data import StoresIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of StoresIdGet200ResponseData from a JSON string
stores_id_get200_response_data_instance = StoresIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print StoresIdGet200ResponseData.to_json()

# convert the object into a dict
stores_id_get200_response_data_dict = stores_id_get200_response_data_instance.to_dict()
# create an instance of StoresIdGet200ResponseData from a dict
stores_id_get200_response_data_form_dict = stores_id_get200_response_data.from_dict(stores_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


