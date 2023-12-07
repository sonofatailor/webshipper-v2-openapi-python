# WaybillsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WaybillsIdGet200ResponseData**](WaybillsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**WaybillsIdGet200ResponseRelationships**](WaybillsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.waybills_id_patch_request import WaybillsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WaybillsIdPatchRequest from a JSON string
waybills_id_patch_request_instance = WaybillsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print WaybillsIdPatchRequest.to_json()

# convert the object into a dict
waybills_id_patch_request_dict = waybills_id_patch_request_instance.to_dict()
# create an instance of WaybillsIdPatchRequest from a dict
waybills_id_patch_request_form_dict = waybills_id_patch_request.from_dict(waybills_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


