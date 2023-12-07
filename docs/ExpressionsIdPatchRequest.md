# ExpressionsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ExpressionsIdGet200ResponseData**](ExpressionsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.expressions_id_patch_request import ExpressionsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExpressionsIdPatchRequest from a JSON string
expressions_id_patch_request_instance = ExpressionsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ExpressionsIdPatchRequest.to_json()

# convert the object into a dict
expressions_id_patch_request_dict = expressions_id_patch_request_instance.to_dict()
# create an instance of ExpressionsIdPatchRequest from a dict
expressions_id_patch_request_form_dict = expressions_id_patch_request.from_dict(expressions_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


