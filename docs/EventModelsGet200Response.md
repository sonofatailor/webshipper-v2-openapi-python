# EventModelsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EventModelsGet200ResponseDataInner]**](EventModelsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.event_models_get200_response import EventModelsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EventModelsGet200Response from a JSON string
event_models_get200_response_instance = EventModelsGet200Response.from_json(json)
# print the JSON string representation of the object
print EventModelsGet200Response.to_json()

# convert the object into a dict
event_models_get200_response_dict = event_models_get200_response_instance.to_dict()
# create an instance of EventModelsGet200Response from a dict
event_models_get200_response_form_dict = event_models_get200_response.from_dict(event_models_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


