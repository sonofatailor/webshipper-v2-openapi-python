# TrackingEvents


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | One of &lt;em&gt;information_received&lt;/em&gt;, &lt;em&gt;in_transit&lt;/em&gt;, &lt;em&gt;out_for_delivery&lt;/em&gt;, &lt;em&gt;customs_clearance_delayed&lt;/em&gt;, &lt;em&gt;attempted_delivery&lt;/em&gt;, &lt;em&gt;ready_for_pickup&lt;/em&gt;, &lt;em&gt;delivered_to_drop_point&lt;/em&gt;, &lt;em&gt;delivered&lt;/em&gt;, &lt;em&gt;returned&lt;/em&gt;, &lt;em&gt;undeliverable&lt;/em&gt; or &lt;em&gt;unknown&lt;/em&gt; | [optional] 
**time** | **str** | Time the event occured at the carrier | [optional] 
**description** | **str** | Readable description of the event | [optional] 
**location** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**tracking_number** | **str** | The tracking number for this event, if availiable | [optional] 
**event_id** | **str** | Unique event of the id | [optional] 
**shipment_id** | **int** | ID of shipment | [optional] 
**tracking_link_id** | **int** |  | [optional] 
**tracking_link_url** | **str** | The tracking link for this event, if availiable | [optional] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 

## Example

```python
from openapi_client.models.tracking_events import TrackingEvents

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingEvents from a JSON string
tracking_events_instance = TrackingEvents.from_json(json)
# print the JSON string representation of the object
print TrackingEvents.to_json()

# convert the object into a dict
tracking_events_dict = tracking_events_instance.to_dict()
# create an instance of TrackingEvents from a dict
tracking_events_form_dict = tracking_events.from_dict(tracking_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


