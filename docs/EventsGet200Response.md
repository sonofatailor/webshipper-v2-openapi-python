# EventsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EventsGet200ResponseDataInner]**](EventsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.events_get200_response import EventsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EventsGet200Response from a JSON string
events_get200_response_instance = EventsGet200Response.from_json(json)
# print the JSON string representation of the object
print EventsGet200Response.to_json()

# convert the object into a dict
events_get200_response_dict = events_get200_response_instance.to_dict()
# create an instance of EventsGet200Response from a dict
events_get200_response_form_dict = events_get200_response.from_dict(events_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


