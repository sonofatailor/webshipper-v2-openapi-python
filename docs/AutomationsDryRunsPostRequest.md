# AutomationsDryRunsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AutomationsDryRunsPostRequestData**](AutomationsDryRunsPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.automations_dry_runs_post_request import AutomationsDryRunsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationsDryRunsPostRequest from a JSON string
automations_dry_runs_post_request_instance = AutomationsDryRunsPostRequest.from_json(json)
# print the JSON string representation of the object
print AutomationsDryRunsPostRequest.to_json()

# convert the object into a dict
automations_dry_runs_post_request_dict = automations_dry_runs_post_request_instance.to_dict()
# create an instance of AutomationsDryRunsPostRequest from a dict
automations_dry_runs_post_request_form_dict = automations_dry_runs_post_request.from_dict(automations_dry_runs_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


