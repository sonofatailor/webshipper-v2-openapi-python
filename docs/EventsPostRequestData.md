# EventsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Events**](Events.md) |  | [optional] 

## Example

```python
from openapi_client.models.events_post_request_data import EventsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of EventsPostRequestData from a JSON string
events_post_request_data_instance = EventsPostRequestData.from_json(json)
# print the JSON string representation of the object
print EventsPostRequestData.to_json()

# convert the object into a dict
events_post_request_data_dict = events_post_request_data_instance.to_dict()
# create an instance of EventsPostRequestData from a dict
events_post_request_data_form_dict = events_post_request_data.from_dict(events_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


