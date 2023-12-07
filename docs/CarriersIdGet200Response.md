# CarriersIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CarriersIdGet200ResponseData**](CarriersIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**CarriersIdGet200ResponseRelationships**](CarriersIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[CarriersIdGet200ResponseIncludedInner]**](CarriersIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.carriers_id_get200_response import CarriersIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CarriersIdGet200Response from a JSON string
carriers_id_get200_response_instance = CarriersIdGet200Response.from_json(json)
# print the JSON string representation of the object
print CarriersIdGet200Response.to_json()

# convert the object into a dict
carriers_id_get200_response_dict = carriers_id_get200_response_instance.to_dict()
# create an instance of CarriersIdGet200Response from a dict
carriers_id_get200_response_form_dict = carriers_id_get200_response.from_dict(carriers_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


