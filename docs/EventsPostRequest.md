# EventsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EventsPostRequestData**](EventsPostRequestData.md) |  | [optional] 
**relationships** | [**EventsIdGet200ResponseRelationships**](EventsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.events_post_request import EventsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventsPostRequest from a JSON string
events_post_request_instance = EventsPostRequest.from_json(json)
# print the JSON string representation of the object
print EventsPostRequest.to_json()

# convert the object into a dict
events_post_request_dict = events_post_request_instance.to_dict()
# create an instance of EventsPostRequest from a dict
events_post_request_form_dict = events_post_request.from_dict(events_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


