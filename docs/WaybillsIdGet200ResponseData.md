# WaybillsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Waybills**](Waybills.md) |  | [optional] 

## Example

```python
from webshipperv2.models.waybills_id_get200_response_data import WaybillsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of WaybillsIdGet200ResponseData from a JSON string
waybills_id_get200_response_data_instance = WaybillsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print WaybillsIdGet200ResponseData.to_json()

# convert the object into a dict
waybills_id_get200_response_data_dict = waybills_id_get200_response_data_instance.to_dict()
# create an instance of WaybillsIdGet200ResponseData from a dict
waybills_id_get200_response_data_form_dict = waybills_id_get200_response_data.from_dict(waybills_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


