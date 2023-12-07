# EventModelsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EventModelsIdGet200ResponseData**](EventModelsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.event_models_id_patch_request import EventModelsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventModelsIdPatchRequest from a JSON string
event_models_id_patch_request_instance = EventModelsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print EventModelsIdPatchRequest.to_json()

# convert the object into a dict
event_models_id_patch_request_dict = event_models_id_patch_request_instance.to_dict()
# create an instance of EventModelsIdPatchRequest from a dict
event_models_id_patch_request_form_dict = event_models_id_patch_request.from_dict(event_models_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


