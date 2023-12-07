# TrackingEventsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TrackingEventsIdGet200ResponseData**](TrackingEventsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**TrackingEventsIdGet200ResponseRelationships**](TrackingEventsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[TrackingEventsIdGet200ResponseIncludedInner]**](TrackingEventsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.tracking_events_id_get200_response import TrackingEventsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingEventsIdGet200Response from a JSON string
tracking_events_id_get200_response_instance = TrackingEventsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print TrackingEventsIdGet200Response.to_json()

# convert the object into a dict
tracking_events_id_get200_response_dict = tracking_events_id_get200_response_instance.to_dict()
# create an instance of TrackingEventsIdGet200Response from a dict
tracking_events_id_get200_response_form_dict = tracking_events_id_get200_response.from_dict(tracking_events_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


