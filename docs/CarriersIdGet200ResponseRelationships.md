# CarriersIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_type** | [**CarriersIdGet200ResponseRelationshipsCarrierType**](CarriersIdGet200ResponseRelationshipsCarrierType.md) |  | [optional] 
**sender_address** | [**CarriersIdGet200ResponseRelationshipsSenderAddress**](CarriersIdGet200ResponseRelationshipsSenderAddress.md) |  | [optional] 
**return_address** | [**CarriersIdGet200ResponseRelationshipsSenderAddress**](CarriersIdGet200ResponseRelationshipsSenderAddress.md) |  | [optional] 

## Example

```python
from webshipperv2.models.carriers_id_get200_response_relationships import CarriersIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CarriersIdGet200ResponseRelationships from a JSON string
carriers_id_get200_response_relationships_instance = CarriersIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print CarriersIdGet200ResponseRelationships.to_json()

# convert the object into a dict
carriers_id_get200_response_relationships_dict = carriers_id_get200_response_relationships_instance.to_dict()
# create an instance of CarriersIdGet200ResponseRelationships from a dict
carriers_id_get200_response_relationships_form_dict = carriers_id_get200_response_relationships.from_dict(carriers_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


