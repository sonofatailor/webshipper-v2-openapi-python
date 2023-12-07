# EventsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Events**](Events.md) |  | [optional] 

## Example

```python
from openapi_client.models.events_id_get200_response_data import EventsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of EventsIdGet200ResponseData from a JSON string
events_id_get200_response_data_instance = EventsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print EventsIdGet200ResponseData.to_json()

# convert the object into a dict
events_id_get200_response_data_dict = events_id_get200_response_data_instance.to_dict()
# create an instance of EventsIdGet200ResponseData from a dict
events_id_get200_response_data_form_dict = events_id_get200_response_data.from_dict(events_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


