# PickupsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PickupsPostRequestData**](PickupsPostRequestData.md) |  | [optional] 
**relationships** | [**PickupsIdGet200ResponseRelationships**](PickupsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.pickups_post_request import PickupsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PickupsPostRequest from a JSON string
pickups_post_request_instance = PickupsPostRequest.from_json(json)
# print the JSON string representation of the object
print PickupsPostRequest.to_json()

# convert the object into a dict
pickups_post_request_dict = pickups_post_request_instance.to_dict()
# create an instance of PickupsPostRequest from a dict
pickups_post_request_form_dict = pickups_post_request.from_dict(pickups_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


