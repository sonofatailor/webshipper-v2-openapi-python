# PickupsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PickupsIdGet200ResponseData**](PickupsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**PickupsIdGet200ResponseRelationships**](PickupsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.pickups_id_patch_request import PickupsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PickupsIdPatchRequest from a JSON string
pickups_id_patch_request_instance = PickupsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print PickupsIdPatchRequest.to_json()

# convert the object into a dict
pickups_id_patch_request_dict = pickups_id_patch_request_instance.to_dict()
# create an instance of PickupsIdPatchRequest from a dict
pickups_id_patch_request_form_dict = pickups_id_patch_request.from_dict(pickups_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


