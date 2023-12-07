# ReturnsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReturnsIdGet200ResponseData**](ReturnsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**ReturnsIdGet200ResponseRelationships**](ReturnsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.returns_id_patch_request import ReturnsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsIdPatchRequest from a JSON string
returns_id_patch_request_instance = ReturnsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ReturnsIdPatchRequest.to_json()

# convert the object into a dict
returns_id_patch_request_dict = returns_id_patch_request_instance.to_dict()
# create an instance of ReturnsIdPatchRequest from a dict
returns_id_patch_request_form_dict = returns_id_patch_request.from_dict(returns_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


