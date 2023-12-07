# TrackingEventsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**TrackingEvents**](TrackingEvents.md) |  | [optional] 

## Example

```python
from openapi_client.models.tracking_events_id_get200_response_data import TrackingEventsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingEventsIdGet200ResponseData from a JSON string
tracking_events_id_get200_response_data_instance = TrackingEventsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print TrackingEventsIdGet200ResponseData.to_json()

# convert the object into a dict
tracking_events_id_get200_response_data_dict = tracking_events_id_get200_response_data_instance.to_dict()
# create an instance of TrackingEventsIdGet200ResponseData from a dict
tracking_events_id_get200_response_data_form_dict = tracking_events_id_get200_response_data.from_dict(tracking_events_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


