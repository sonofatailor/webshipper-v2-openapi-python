# ShippingMappingsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**ShippingMappings**](ShippingMappings.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipping_mappings_id_get200_response_data import ShippingMappingsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingMappingsIdGet200ResponseData from a JSON string
shipping_mappings_id_get200_response_data_instance = ShippingMappingsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print ShippingMappingsIdGet200ResponseData.to_json()

# convert the object into a dict
shipping_mappings_id_get200_response_data_dict = shipping_mappings_id_get200_response_data_instance.to_dict()
# create an instance of ShippingMappingsIdGet200ResponseData from a dict
shipping_mappings_id_get200_response_data_form_dict = shipping_mappings_id_get200_response_data.from_dict(shipping_mappings_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


