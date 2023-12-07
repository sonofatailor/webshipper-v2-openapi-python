# CarrierTypesGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CarrierTypesGet200ResponseDataInner]**](CarrierTypesGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.carrier_types_get200_response import CarrierTypesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CarrierTypesGet200Response from a JSON string
carrier_types_get200_response_instance = CarrierTypesGet200Response.from_json(json)
# print the JSON string representation of the object
print CarrierTypesGet200Response.to_json()

# convert the object into a dict
carrier_types_get200_response_dict = carrier_types_get200_response_instance.to_dict()
# create an instance of CarrierTypesGet200Response from a dict
carrier_types_get200_response_form_dict = carrier_types_get200_response.from_dict(carrier_types_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


