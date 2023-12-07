# RegionsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RegionsIdGet200ResponseData**](RegionsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**RegionsIdGet200ResponseRelationships**](RegionsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.regions_id_patch_request import RegionsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegionsIdPatchRequest from a JSON string
regions_id_patch_request_instance = RegionsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print RegionsIdPatchRequest.to_json()

# convert the object into a dict
regions_id_patch_request_dict = regions_id_patch_request_instance.to_dict()
# create an instance of RegionsIdPatchRequest from a dict
regions_id_patch_request_form_dict = regions_id_patch_request.from_dict(regions_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


