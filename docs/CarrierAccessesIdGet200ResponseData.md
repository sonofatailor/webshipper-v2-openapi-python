# CarrierAccessesIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**CarrierAccesses**](CarrierAccesses.md) |  | [optional] 

## Example

```python
from webshipperv2.models.carrier_accesses_id_get200_response_data import CarrierAccessesIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CarrierAccessesIdGet200ResponseData from a JSON string
carrier_accesses_id_get200_response_data_instance = CarrierAccessesIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print CarrierAccessesIdGet200ResponseData.to_json()

# convert the object into a dict
carrier_accesses_id_get200_response_data_dict = carrier_accesses_id_get200_response_data_instance.to_dict()
# create an instance of CarrierAccessesIdGet200ResponseData from a dict
carrier_accesses_id_get200_response_data_form_dict = carrier_accesses_id_get200_response_data.from_dict(carrier_accesses_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


