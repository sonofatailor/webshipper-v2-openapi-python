# ShipmentsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ShipmentsPostRequestData**](ShipmentsPostRequestData.md) |  | [optional] 
**relationships** | [**ShipmentsIdGet200ResponseRelationships**](ShipmentsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipments_post_request import ShipmentsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentsPostRequest from a JSON string
shipments_post_request_instance = ShipmentsPostRequest.from_json(json)
# print the JSON string representation of the object
print ShipmentsPostRequest.to_json()

# convert the object into a dict
shipments_post_request_dict = shipments_post_request_instance.to_dict()
# create an instance of ShipmentsPostRequest from a dict
shipments_post_request_form_dict = shipments_post_request.from_dict(shipments_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


