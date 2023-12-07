# WaybillsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WaybillsIdGet200ResponseData**](WaybillsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**WaybillsIdGet200ResponseRelationships**](WaybillsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[WaybillsIdGet200ResponseIncludedInner]**](WaybillsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.waybills_id_get200_response import WaybillsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of WaybillsIdGet200Response from a JSON string
waybills_id_get200_response_instance = WaybillsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print WaybillsIdGet200Response.to_json()

# convert the object into a dict
waybills_id_get200_response_dict = waybills_id_get200_response_instance.to_dict()
# create an instance of WaybillsIdGet200Response from a dict
waybills_id_get200_response_form_dict = waybills_id_get200_response.from_dict(waybills_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


