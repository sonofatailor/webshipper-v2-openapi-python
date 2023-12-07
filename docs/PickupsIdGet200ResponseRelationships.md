# PickupsIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | [**BarcodeRangesIdGet200ResponseRelationshipsCarrier**](BarcodeRangesIdGet200ResponseRelationshipsCarrier.md) |  | [optional] 
**shipping_address** | [**CarriersIdGet200ResponseRelationshipsSenderAddress**](CarriersIdGet200ResponseRelationshipsSenderAddress.md) |  | [optional] 

## Example

```python
from webshipperv2.models.pickups_id_get200_response_relationships import PickupsIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of PickupsIdGet200ResponseRelationships from a JSON string
pickups_id_get200_response_relationships_instance = PickupsIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print PickupsIdGet200ResponseRelationships.to_json()

# convert the object into a dict
pickups_id_get200_response_relationships_dict = pickups_id_get200_response_relationships_instance.to_dict()
# create an instance of PickupsIdGet200ResponseRelationships from a dict
pickups_id_get200_response_relationships_form_dict = pickups_id_get200_response_relationships.from_dict(pickups_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


