# StoresIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender_address** | [**CarriersIdGet200ResponseRelationshipsSenderAddress**](CarriersIdGet200ResponseRelationshipsSenderAddress.md) |  | [optional] 
**return_address** | [**CarriersIdGet200ResponseRelationshipsSenderAddress**](CarriersIdGet200ResponseRelationshipsSenderAddress.md) |  | [optional] 
**pickup_address** | [**CarriersIdGet200ResponseRelationshipsSenderAddress**](CarriersIdGet200ResponseRelationshipsSenderAddress.md) |  | [optional] 
**sold_from_address** | [**CarriersIdGet200ResponseRelationshipsSenderAddress**](CarriersIdGet200ResponseRelationshipsSenderAddress.md) |  | [optional] 

## Example

```python
from openapi_client.models.stores_id_get200_response_relationships import StoresIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of StoresIdGet200ResponseRelationships from a JSON string
stores_id_get200_response_relationships_instance = StoresIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print StoresIdGet200ResponseRelationships.to_json()

# convert the object into a dict
stores_id_get200_response_relationships_dict = stores_id_get200_response_relationships_instance.to_dict()
# create an instance of StoresIdGet200ResponseRelationships from a dict
stores_id_get200_response_relationships_form_dict = stores_id_get200_response_relationships.from_dict(stores_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


