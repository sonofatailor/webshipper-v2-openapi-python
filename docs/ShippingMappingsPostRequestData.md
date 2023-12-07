# ShippingMappingsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**ShippingMappings**](ShippingMappings.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipping_mappings_post_request_data import ShippingMappingsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingMappingsPostRequestData from a JSON string
shipping_mappings_post_request_data_instance = ShippingMappingsPostRequestData.from_json(json)
# print the JSON string representation of the object
print ShippingMappingsPostRequestData.to_json()

# convert the object into a dict
shipping_mappings_post_request_data_dict = shipping_mappings_post_request_data_instance.to_dict()
# create an instance of ShippingMappingsPostRequestData from a dict
shipping_mappings_post_request_data_form_dict = shipping_mappings_post_request_data.from_dict(shipping_mappings_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


