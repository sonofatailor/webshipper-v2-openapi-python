# ActionsIdGet200ResponseIncludedInnerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger** | **object** | Flattened resource of type Trigger | [optional] 
**actions** | **List[str]** | Array of flattened resources of type Action  | [optional] 
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**priority** | **int** |  | [optional] 
**automation_type** | **int** |  | [optional] 

## Example

```python
from webshipperv2.models.actions_id_get200_response_included_inner_data import ActionsIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsIdGet200ResponseIncludedInnerData from a JSON string
actions_id_get200_response_included_inner_data_instance = ActionsIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print ActionsIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
actions_id_get200_response_included_inner_data_dict = actions_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of ActionsIdGet200ResponseIncludedInnerData from a dict
actions_id_get200_response_included_inner_data_form_dict = actions_id_get200_response_included_inner_data.from_dict(actions_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


