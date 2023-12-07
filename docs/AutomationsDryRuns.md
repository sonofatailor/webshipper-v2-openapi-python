# AutomationsDryRuns


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **str** |  | [optional] 
**automation** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**report_id** | **str** |  | [optional] 
**model_type** | **str** |  | [optional] 
**element_name** | **str** |  | [optional] 

## Example

```python
from webshipperv2.models.automations_dry_runs import AutomationsDryRuns

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationsDryRuns from a JSON string
automations_dry_runs_instance = AutomationsDryRuns.from_json(json)
# print the JSON string representation of the object
print AutomationsDryRuns.to_json()

# convert the object into a dict
automations_dry_runs_dict = automations_dry_runs_instance.to_dict()
# create an instance of AutomationsDryRuns from a dict
automations_dry_runs_form_dict = automations_dry_runs.from_dict(automations_dry_runs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


