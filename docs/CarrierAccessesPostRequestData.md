# CarrierAccessesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**CarrierAccesses**](CarrierAccesses.md) |  | [optional] 

## Example

```python
from openapi_client.models.carrier_accesses_post_request_data import CarrierAccessesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CarrierAccessesPostRequestData from a JSON string
carrier_accesses_post_request_data_instance = CarrierAccessesPostRequestData.from_json(json)
# print the JSON string representation of the object
print CarrierAccessesPostRequestData.to_json()

# convert the object into a dict
carrier_accesses_post_request_data_dict = carrier_accesses_post_request_data_instance.to_dict()
# create an instance of CarrierAccessesPostRequestData from a dict
carrier_accesses_post_request_data_form_dict = carrier_accesses_post_request_data.from_dict(carrier_accesses_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


