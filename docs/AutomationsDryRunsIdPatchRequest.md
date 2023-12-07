# AutomationsDryRunsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AutomationsDryRunsIdGet200ResponseData**](AutomationsDryRunsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.automations_dry_runs_id_patch_request import AutomationsDryRunsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationsDryRunsIdPatchRequest from a JSON string
automations_dry_runs_id_patch_request_instance = AutomationsDryRunsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print AutomationsDryRunsIdPatchRequest.to_json()

# convert the object into a dict
automations_dry_runs_id_patch_request_dict = automations_dry_runs_id_patch_request_instance.to_dict()
# create an instance of AutomationsDryRunsIdPatchRequest from a dict
automations_dry_runs_id_patch_request_form_dict = automations_dry_runs_id_patch_request.from_dict(automations_dry_runs_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


