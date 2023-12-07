# ShipmentsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ShipmentsGet200ResponseDataInner]**](ShipmentsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.shipments_get200_response import ShipmentsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentsGet200Response from a JSON string
shipments_get200_response_instance = ShipmentsGet200Response.from_json(json)
# print the JSON string representation of the object
print ShipmentsGet200Response.to_json()

# convert the object into a dict
shipments_get200_response_dict = shipments_get200_response_instance.to_dict()
# create an instance of ShipmentsGet200Response from a dict
shipments_get200_response_form_dict = shipments_get200_response.from_dict(shipments_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


