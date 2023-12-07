# LocalAttrsIdGet200ResponseIncludedInnerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**support_url** | **str** |  | [optional] 
**public_global_attrs** | **str** |  | [optional] 
**list_logo** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**module_link** | **str** |  | [optional] 
**can_autofulfill** | **bool** |  | [optional] 
**can_limit_drop_points** | **bool** |  | [optional] 
**supports_rate_quoting** | **bool** |  | [optional] 
**uses_scheduled_import** | **bool** |  | [optional] 
**supports_time_interval_import** | **bool** |  | [optional] 
**supports_statuses_import** | **bool** |  | [optional] 
**supports_id_import** | **bool** |  | [optional] 
**supports_vat_in_checkout** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.local_attrs_id_get200_response_included_inner_data import LocalAttrsIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of LocalAttrsIdGet200ResponseIncludedInnerData from a JSON string
local_attrs_id_get200_response_included_inner_data_instance = LocalAttrsIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print LocalAttrsIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
local_attrs_id_get200_response_included_inner_data_dict = local_attrs_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of LocalAttrsIdGet200ResponseIncludedInnerData from a dict
local_attrs_id_get200_response_included_inner_data_form_dict = local_attrs_id_get200_response_included_inner_data.from_dict(local_attrs_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


