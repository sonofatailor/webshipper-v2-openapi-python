# WaybillsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WaybillsPostRequestData**](WaybillsPostRequestData.md) |  | [optional] 
**relationships** | [**WaybillsIdGet200ResponseRelationships**](WaybillsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.waybills_post_request import WaybillsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WaybillsPostRequest from a JSON string
waybills_post_request_instance = WaybillsPostRequest.from_json(json)
# print the JSON string representation of the object
print WaybillsPostRequest.to_json()

# convert the object into a dict
waybills_post_request_dict = waybills_post_request_instance.to_dict()
# create an instance of WaybillsPostRequest from a dict
waybills_post_request_form_dict = waybills_post_request.from_dict(waybills_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


