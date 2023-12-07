# CarrierAccessesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CarrierAccessesPostRequestData**](CarrierAccessesPostRequestData.md) |  | [optional] 
**relationships** | [**CarrierAccessesIdGet200ResponseRelationships**](CarrierAccessesIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.carrier_accesses_post_request import CarrierAccessesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CarrierAccessesPostRequest from a JSON string
carrier_accesses_post_request_instance = CarrierAccessesPostRequest.from_json(json)
# print the JSON string representation of the object
print CarrierAccessesPostRequest.to_json()

# convert the object into a dict
carrier_accesses_post_request_dict = carrier_accesses_post_request_instance.to_dict()
# create an instance of CarrierAccessesPostRequest from a dict
carrier_accesses_post_request_form_dict = carrier_accesses_post_request.from_dict(carrier_accesses_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


