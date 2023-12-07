# EventModelsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.event_models_id_get200_response_data import EventModelsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of EventModelsIdGet200ResponseData from a JSON string
event_models_id_get200_response_data_instance = EventModelsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print EventModelsIdGet200ResponseData.to_json()

# convert the object into a dict
event_models_id_get200_response_data_dict = event_models_id_get200_response_data_instance.to_dict()
# create an instance of EventModelsIdGet200ResponseData from a dict
event_models_id_get200_response_data_form_dict = event_models_id_get200_response_data.from_dict(event_models_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


