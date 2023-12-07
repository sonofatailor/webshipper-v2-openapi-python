# TrackingEventsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TrackingEventsGet200ResponseDataInner]**](TrackingEventsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.tracking_events_get200_response import TrackingEventsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingEventsGet200Response from a JSON string
tracking_events_get200_response_instance = TrackingEventsGet200Response.from_json(json)
# print the JSON string representation of the object
print TrackingEventsGet200Response.to_json()

# convert the object into a dict
tracking_events_get200_response_dict = tracking_events_get200_response_instance.to_dict()
# create an instance of TrackingEventsGet200Response from a dict
tracking_events_get200_response_form_dict = tracking_events_get200_response.from_dict(tracking_events_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


