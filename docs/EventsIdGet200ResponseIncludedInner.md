# EventsIdGet200ResponseIncludedInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**data** | [**EventsIdGet200ResponseIncludedInnerData**](EventsIdGet200ResponseIncludedInnerData.md) |  | [optional] 

## Example

```python
from openapi_client.models.events_id_get200_response_included_inner import EventsIdGet200ResponseIncludedInner

# TODO update the JSON string below
json = "{}"
# create an instance of EventsIdGet200ResponseIncludedInner from a JSON string
events_id_get200_response_included_inner_instance = EventsIdGet200ResponseIncludedInner.from_json(json)
# print the JSON string representation of the object
print EventsIdGet200ResponseIncludedInner.to_json()

# convert the object into a dict
events_id_get200_response_included_inner_dict = events_id_get200_response_included_inner_instance.to_dict()
# create an instance of EventsIdGet200ResponseIncludedInner from a dict
events_id_get200_response_included_inner_form_dict = events_id_get200_response_included_inner.from_dict(events_id_get200_response_included_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


