# ShipmentsTrackingLinksInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**latest_transit_event** | **str** |  | [optional] 
**tracking_events** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipments_tracking_links_inner import ShipmentsTrackingLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentsTrackingLinksInner from a JSON string
shipments_tracking_links_inner_instance = ShipmentsTrackingLinksInner.from_json(json)
# print the JSON string representation of the object
print ShipmentsTrackingLinksInner.to_json()

# convert the object into a dict
shipments_tracking_links_inner_dict = shipments_tracking_links_inner_instance.to_dict()
# create an instance of ShipmentsTrackingLinksInner from a dict
shipments_tracking_links_inner_form_dict = shipments_tracking_links_inner.from_dict(shipments_tracking_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


