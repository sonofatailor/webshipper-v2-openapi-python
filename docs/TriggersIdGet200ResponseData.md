# TriggersIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Triggers**](Triggers.md) |  | [optional] 

## Example

```python
from webshipperv2.models.triggers_id_get200_response_data import TriggersIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TriggersIdGet200ResponseData from a JSON string
triggers_id_get200_response_data_instance = TriggersIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print TriggersIdGet200ResponseData.to_json()

# convert the object into a dict
triggers_id_get200_response_data_dict = triggers_id_get200_response_data_instance.to_dict()
# create an instance of TriggersIdGet200ResponseData from a dict
triggers_id_get200_response_data_form_dict = triggers_id_get200_response_data.from_dict(triggers_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


