# EventModelsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EventModelsIdGet200ResponseData**](EventModelsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.event_models_id_get200_response import EventModelsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EventModelsIdGet200Response from a JSON string
event_models_id_get200_response_instance = EventModelsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print EventModelsIdGet200Response.to_json()

# convert the object into a dict
event_models_id_get200_response_dict = event_models_id_get200_response_instance.to_dict()
# create an instance of EventModelsIdGet200Response from a dict
event_models_id_get200_response_form_dict = event_models_id_get200_response.from_dict(event_models_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


