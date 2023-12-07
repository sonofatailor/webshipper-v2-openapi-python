# EventModelsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EventModelsPostRequestData**](EventModelsPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.event_models_post_request import EventModelsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventModelsPostRequest from a JSON string
event_models_post_request_instance = EventModelsPostRequest.from_json(json)
# print the JSON string representation of the object
print EventModelsPostRequest.to_json()

# convert the object into a dict
event_models_post_request_dict = event_models_post_request_instance.to_dict()
# create an instance of EventModelsPostRequest from a dict
event_models_post_request_form_dict = event_models_post_request.from_dict(event_models_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


