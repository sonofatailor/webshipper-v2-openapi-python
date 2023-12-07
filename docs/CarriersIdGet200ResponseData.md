# CarriersIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Carriers**](Carriers.md) |  | [optional] 

## Example

```python
from openapi_client.models.carriers_id_get200_response_data import CarriersIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CarriersIdGet200ResponseData from a JSON string
carriers_id_get200_response_data_instance = CarriersIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print CarriersIdGet200ResponseData.to_json()

# convert the object into a dict
carriers_id_get200_response_data_dict = carriers_id_get200_response_data_instance.to_dict()
# create an instance of CarriersIdGet200ResponseData from a dict
carriers_id_get200_response_data_form_dict = carriers_id_get200_response_data.from_dict(carriers_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


