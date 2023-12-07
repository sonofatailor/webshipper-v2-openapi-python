# EventsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EventsIdGet200ResponseData**](EventsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**EventsIdGet200ResponseRelationships**](EventsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.events_id_patch_request import EventsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventsIdPatchRequest from a JSON string
events_id_patch_request_instance = EventsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print EventsIdPatchRequest.to_json()

# convert the object into a dict
events_id_patch_request_dict = events_id_patch_request_instance.to_dict()
# create an instance of EventsIdPatchRequest from a dict
events_id_patch_request_form_dict = events_id_patch_request.from_dict(events_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


