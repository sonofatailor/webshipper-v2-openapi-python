# ShipmentsGet200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Shipments**](Shipments.md) |  | [optional] 

## Example

```python
from webshipperv2.models.shipments_get200_response_data_inner import ShipmentsGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentsGet200ResponseDataInner from a JSON string
shipments_get200_response_data_inner_instance = ShipmentsGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print ShipmentsGet200ResponseDataInner.to_json()

# convert the object into a dict
shipments_get200_response_data_inner_dict = shipments_get200_response_data_inner_instance.to_dict()
# create an instance of ShipmentsGet200ResponseDataInner from a dict
shipments_get200_response_data_inner_form_dict = shipments_get200_response_data_inner.from_dict(shipments_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


