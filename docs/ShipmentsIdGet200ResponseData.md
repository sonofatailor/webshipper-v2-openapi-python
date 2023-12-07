# ShipmentsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Shipments**](Shipments.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipments_id_get200_response_data import ShipmentsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentsIdGet200ResponseData from a JSON string
shipments_id_get200_response_data_instance = ShipmentsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print ShipmentsIdGet200ResponseData.to_json()

# convert the object into a dict
shipments_id_get200_response_data_dict = shipments_id_get200_response_data_instance.to_dict()
# create an instance of ShipmentsIdGet200ResponseData from a dict
shipments_id_get200_response_data_form_dict = shipments_id_get200_response_data.from_dict(shipments_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


