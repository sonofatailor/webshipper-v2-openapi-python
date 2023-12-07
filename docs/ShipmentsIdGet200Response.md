# ShipmentsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ShipmentsIdGet200ResponseData**](ShipmentsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**ShipmentsIdGet200ResponseRelationships**](ShipmentsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[ShipmentsIdGet200ResponseIncludedInner]**](ShipmentsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipments_id_get200_response import ShipmentsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentsIdGet200Response from a JSON string
shipments_id_get200_response_instance = ShipmentsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print ShipmentsIdGet200Response.to_json()

# convert the object into a dict
shipments_id_get200_response_dict = shipments_id_get200_response_instance.to_dict()
# create an instance of ShipmentsIdGet200Response from a dict
shipments_id_get200_response_form_dict = shipments_id_get200_response.from_dict(shipments_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


