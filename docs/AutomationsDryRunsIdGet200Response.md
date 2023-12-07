# AutomationsDryRunsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AutomationsDryRunsIdGet200ResponseData**](AutomationsDryRunsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.automations_dry_runs_id_get200_response import AutomationsDryRunsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationsDryRunsIdGet200Response from a JSON string
automations_dry_runs_id_get200_response_instance = AutomationsDryRunsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print AutomationsDryRunsIdGet200Response.to_json()

# convert the object into a dict
automations_dry_runs_id_get200_response_dict = automations_dry_runs_id_get200_response_instance.to_dict()
# create an instance of AutomationsDryRunsIdGet200Response from a dict
automations_dry_runs_id_get200_response_form_dict = automations_dry_runs_id_get200_response.from_dict(automations_dry_runs_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


