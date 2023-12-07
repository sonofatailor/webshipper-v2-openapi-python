# ShipmentsIdGet200ResponseIncludedInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**data** | [**ShipmentsIdGet200ResponseIncludedInnerData**](ShipmentsIdGet200ResponseIncludedInnerData.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipments_id_get200_response_included_inner import ShipmentsIdGet200ResponseIncludedInner

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentsIdGet200ResponseIncludedInner from a JSON string
shipments_id_get200_response_included_inner_instance = ShipmentsIdGet200ResponseIncludedInner.from_json(json)
# print the JSON string representation of the object
print ShipmentsIdGet200ResponseIncludedInner.to_json()

# convert the object into a dict
shipments_id_get200_response_included_inner_dict = shipments_id_get200_response_included_inner_instance.to_dict()
# create an instance of ShipmentsIdGet200ResponseIncludedInner from a dict
shipments_id_get200_response_included_inner_form_dict = shipments_id_get200_response_included_inner.from_dict(shipments_id_get200_response_included_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


