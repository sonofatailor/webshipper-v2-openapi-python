# PickupsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Pickups**](Pickups.md) |  | [optional] 

## Example

```python
from webshipperv2.models.pickups_post_request_data import PickupsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of PickupsPostRequestData from a JSON string
pickups_post_request_data_instance = PickupsPostRequestData.from_json(json)
# print the JSON string representation of the object
print PickupsPostRequestData.to_json()

# convert the object into a dict
pickups_post_request_data_dict = pickups_post_request_data_instance.to_dict()
# create an instance of PickupsPostRequestData from a dict
pickups_post_request_data_form_dict = pickups_post_request_data.from_dict(pickups_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


