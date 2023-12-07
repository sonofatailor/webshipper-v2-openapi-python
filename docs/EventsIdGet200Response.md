# EventsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EventsIdGet200ResponseData**](EventsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**EventsIdGet200ResponseRelationships**](EventsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[EventsIdGet200ResponseIncludedInner]**](EventsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.events_id_get200_response import EventsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EventsIdGet200Response from a JSON string
events_id_get200_response_instance = EventsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print EventsIdGet200Response.to_json()

# convert the object into a dict
events_id_get200_response_dict = events_id_get200_response_instance.to_dict()
# create an instance of EventsIdGet200Response from a dict
events_id_get200_response_form_dict = events_id_get200_response.from_dict(events_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


