# AutomationsDryRunsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AutomationsDryRunsGet200ResponseDataInner]**](AutomationsDryRunsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.automations_dry_runs_get200_response import AutomationsDryRunsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationsDryRunsGet200Response from a JSON string
automations_dry_runs_get200_response_instance = AutomationsDryRunsGet200Response.from_json(json)
# print the JSON string representation of the object
print AutomationsDryRunsGet200Response.to_json()

# convert the object into a dict
automations_dry_runs_get200_response_dict = automations_dry_runs_get200_response_instance.to_dict()
# create an instance of AutomationsDryRunsGet200Response from a dict
automations_dry_runs_get200_response_form_dict = automations_dry_runs_get200_response.from_dict(automations_dry_runs_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


