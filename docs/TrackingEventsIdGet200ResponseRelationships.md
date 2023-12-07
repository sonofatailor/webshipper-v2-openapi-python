# TrackingEventsIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package** | [**TrackingEventsIdGet200ResponseRelationshipsPackage**](TrackingEventsIdGet200ResponseRelationshipsPackage.md) |  | [optional] 
**shipment** | [**EdisIdGet200ResponseRelationshipsShipment**](EdisIdGet200ResponseRelationshipsShipment.md) |  | [optional] 

## Example

```python
from webshipperv2.models.tracking_events_id_get200_response_relationships import TrackingEventsIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingEventsIdGet200ResponseRelationships from a JSON string
tracking_events_id_get200_response_relationships_instance = TrackingEventsIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print TrackingEventsIdGet200ResponseRelationships.to_json()

# convert the object into a dict
tracking_events_id_get200_response_relationships_dict = tracking_events_id_get200_response_relationships_instance.to_dict()
# create an instance of TrackingEventsIdGet200ResponseRelationships from a dict
tracking_events_id_get200_response_relationships_form_dict = tracking_events_id_get200_response_relationships.from_dict(tracking_events_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


