# WaybillsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Waybills**](Waybills.md) |  | [optional] 

## Example

```python
from webshipperv2.models.waybills_post_request_data import WaybillsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of WaybillsPostRequestData from a JSON string
waybills_post_request_data_instance = WaybillsPostRequestData.from_json(json)
# print the JSON string representation of the object
print WaybillsPostRequestData.to_json()

# convert the object into a dict
waybills_post_request_data_dict = waybills_post_request_data_instance.to_dict()
# create an instance of WaybillsPostRequestData from a dict
waybills_post_request_data_form_dict = waybills_post_request_data.from_dict(waybills_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


