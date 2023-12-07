# EventModelsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.event_models_post_request_data import EventModelsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of EventModelsPostRequestData from a JSON string
event_models_post_request_data_instance = EventModelsPostRequestData.from_json(json)
# print the JSON string representation of the object
print EventModelsPostRequestData.to_json()

# convert the object into a dict
event_models_post_request_data_dict = event_models_post_request_data_instance.to_dict()
# create an instance of EventModelsPostRequestData from a dict
event_models_post_request_data_form_dict = event_models_post_request_data.from_dict(event_models_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


