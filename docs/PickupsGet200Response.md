# PickupsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PickupsGet200ResponseDataInner]**](PickupsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.pickups_get200_response import PickupsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PickupsGet200Response from a JSON string
pickups_get200_response_instance = PickupsGet200Response.from_json(json)
# print the JSON string representation of the object
print PickupsGet200Response.to_json()

# convert the object into a dict
pickups_get200_response_dict = pickups_get200_response_instance.to_dict()
# create an instance of PickupsGet200Response from a dict
pickups_get200_response_form_dict = pickups_get200_response.from_dict(pickups_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


