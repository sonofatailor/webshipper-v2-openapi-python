# WaybillsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WaybillsGet200ResponseDataInner]**](WaybillsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.waybills_get200_response import WaybillsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of WaybillsGet200Response from a JSON string
waybills_get200_response_instance = WaybillsGet200Response.from_json(json)
# print the JSON string representation of the object
print WaybillsGet200Response.to_json()

# convert the object into a dict
waybills_get200_response_dict = waybills_get200_response_instance.to_dict()
# create an instance of WaybillsGet200Response from a dict
waybills_get200_response_form_dict = waybills_get200_response.from_dict(waybills_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


