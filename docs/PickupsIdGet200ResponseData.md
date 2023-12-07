# PickupsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Pickups**](Pickups.md) |  | [optional] 

## Example

```python
from webshipperv2.models.pickups_id_get200_response_data import PickupsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PickupsIdGet200ResponseData from a JSON string
pickups_id_get200_response_data_instance = PickupsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print PickupsIdGet200ResponseData.to_json()

# convert the object into a dict
pickups_id_get200_response_data_dict = pickups_id_get200_response_data_instance.to_dict()
# create an instance of PickupsIdGet200ResponseData from a dict
pickups_id_get200_response_data_form_dict = pickups_id_get200_response_data.from_dict(pickups_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


