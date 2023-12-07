# ShipmentsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Shipments**](Shipments.md) |  | [optional] 

## Example

```python
from webshipperv2.models.shipments_post_request_data import ShipmentsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentsPostRequestData from a JSON string
shipments_post_request_data_instance = ShipmentsPostRequestData.from_json(json)
# print the JSON string representation of the object
print ShipmentsPostRequestData.to_json()

# convert the object into a dict
shipments_post_request_data_dict = shipments_post_request_data_instance.to_dict()
# create an instance of ShipmentsPostRequestData from a dict
shipments_post_request_data_form_dict = shipments_post_request_data.from_dict(shipments_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


