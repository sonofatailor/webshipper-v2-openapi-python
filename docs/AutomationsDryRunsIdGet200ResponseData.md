# AutomationsDryRunsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**AutomationsDryRuns**](AutomationsDryRuns.md) |  | [optional] 

## Example

```python
from openapi_client.models.automations_dry_runs_id_get200_response_data import AutomationsDryRunsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationsDryRunsIdGet200ResponseData from a JSON string
automations_dry_runs_id_get200_response_data_instance = AutomationsDryRunsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print AutomationsDryRunsIdGet200ResponseData.to_json()

# convert the object into a dict
automations_dry_runs_id_get200_response_data_dict = automations_dry_runs_id_get200_response_data_instance.to_dict()
# create an instance of AutomationsDryRunsIdGet200ResponseData from a dict
automations_dry_runs_id_get200_response_data_form_dict = automations_dry_runs_id_get200_response_data.from_dict(automations_dry_runs_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


