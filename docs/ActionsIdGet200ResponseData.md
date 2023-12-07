# ActionsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Actions**](Actions.md) |  | [optional] 

## Example

```python
from webshipperv2.models.actions_id_get200_response_data import ActionsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsIdGet200ResponseData from a JSON string
actions_id_get200_response_data_instance = ActionsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print ActionsIdGet200ResponseData.to_json()

# convert the object into a dict
actions_id_get200_response_data_dict = actions_id_get200_response_data_instance.to_dict()
# create an instance of ActionsIdGet200ResponseData from a dict
actions_id_get200_response_data_form_dict = actions_id_get200_response_data.from_dict(actions_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


