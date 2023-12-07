# PickupsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PickupsIdGet200ResponseData**](PickupsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**PickupsIdGet200ResponseRelationships**](PickupsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[PickupsIdGet200ResponseIncludedInner]**](PickupsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.pickups_id_get200_response import PickupsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PickupsIdGet200Response from a JSON string
pickups_id_get200_response_instance = PickupsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print PickupsIdGet200Response.to_json()

# convert the object into a dict
pickups_id_get200_response_dict = pickups_id_get200_response_instance.to_dict()
# create an instance of PickupsIdGet200Response from a dict
pickups_id_get200_response_form_dict = pickups_id_get200_response.from_dict(pickups_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


