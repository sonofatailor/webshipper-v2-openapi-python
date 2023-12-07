# Automations


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
from openapi_client.models.automations import Automations

# TODO update the JSON string below
json = "{}"
# create an instance of Automations from a JSON string
automations_instance = Automations.from_json(json)
# print the JSON string representation of the object
print Automations.to_json()

# convert the object into a dict
automations_dict = automations_instance.to_dict()
# create an instance of Automations from a dict
automations_form_dict = automations.from_dict(automations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


