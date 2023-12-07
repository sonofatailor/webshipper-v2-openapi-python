# CarrierAccessesIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | [**BarcodeRangesIdGet200ResponseRelationshipsCarrier**](BarcodeRangesIdGet200ResponseRelationshipsCarrier.md) |  | [optional] 
**user** | [**CarrierAccessesIdGet200ResponseRelationshipsUser**](CarrierAccessesIdGet200ResponseRelationshipsUser.md) |  | [optional] 

## Example

```python
from webshipperv2.models.carrier_accesses_id_get200_response_relationships import CarrierAccessesIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CarrierAccessesIdGet200ResponseRelationships from a JSON string
carrier_accesses_id_get200_response_relationships_instance = CarrierAccessesIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print CarrierAccessesIdGet200ResponseRelationships.to_json()

# convert the object into a dict
carrier_accesses_id_get200_response_relationships_dict = carrier_accesses_id_get200_response_relationships_instance.to_dict()
# create an instance of CarrierAccessesIdGet200ResponseRelationships from a dict
carrier_accesses_id_get200_response_relationships_form_dict = carrier_accesses_id_get200_response_relationships.from_dict(carrier_accesses_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


