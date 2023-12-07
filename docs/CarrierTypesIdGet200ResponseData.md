# CarrierTypesIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**CarrierTypes**](CarrierTypes.md) |  | [optional] 

## Example

```python
from openapi_client.models.carrier_types_id_get200_response_data import CarrierTypesIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CarrierTypesIdGet200ResponseData from a JSON string
carrier_types_id_get200_response_data_instance = CarrierTypesIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print CarrierTypesIdGet200ResponseData.to_json()

# convert the object into a dict
carrier_types_id_get200_response_data_dict = carrier_types_id_get200_response_data_instance.to_dict()
# create an instance of CarrierTypesIdGet200ResponseData from a dict
carrier_types_id_get200_response_data_form_dict = carrier_types_id_get200_response_data.from_dict(carrier_types_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


