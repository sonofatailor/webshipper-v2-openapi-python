# PickupsIdGet200ResponseIncludedInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**data** | [**PickupsIdGet200ResponseIncludedInnerData**](PickupsIdGet200ResponseIncludedInnerData.md) |  | [optional] 

## Example

```python
from webshipperv2.models.pickups_id_get200_response_included_inner import PickupsIdGet200ResponseIncludedInner

# TODO update the JSON string below
json = "{}"
# create an instance of PickupsIdGet200ResponseIncludedInner from a JSON string
pickups_id_get200_response_included_inner_instance = PickupsIdGet200ResponseIncludedInner.from_json(json)
# print the JSON string representation of the object
print PickupsIdGet200ResponseIncludedInner.to_json()

# convert the object into a dict
pickups_id_get200_response_included_inner_dict = pickups_id_get200_response_included_inner_instance.to_dict()
# create an instance of PickupsIdGet200ResponseIncludedInner from a dict
pickups_id_get200_response_included_inner_form_dict = pickups_id_get200_response_included_inner.from_dict(pickups_id_get200_response_included_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


