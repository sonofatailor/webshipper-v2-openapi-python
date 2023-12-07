# AutomationsDryRunsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**AutomationsDryRuns**](AutomationsDryRuns.md) |  | [optional] 

## Example

```python
from webshipperv2.models.automations_dry_runs_post_request_data import AutomationsDryRunsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationsDryRunsPostRequestData from a JSON string
automations_dry_runs_post_request_data_instance = AutomationsDryRunsPostRequestData.from_json(json)
# print the JSON string representation of the object
print AutomationsDryRunsPostRequestData.to_json()

# convert the object into a dict
automations_dry_runs_post_request_data_dict = automations_dry_runs_post_request_data_instance.to_dict()
# create an instance of AutomationsDryRunsPostRequestData from a dict
automations_dry_runs_post_request_data_form_dict = automations_dry_runs_post_request_data.from_dict(automations_dry_runs_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


