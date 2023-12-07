# ShippingRatesIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ShippingRatesIdGet200ResponseData**](ShippingRatesIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**ShippingRatesIdGet200ResponseRelationships**](ShippingRatesIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipping_rates_id_patch_request import ShippingRatesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingRatesIdPatchRequest from a JSON string
shipping_rates_id_patch_request_instance = ShippingRatesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ShippingRatesIdPatchRequest.to_json()

# convert the object into a dict
shipping_rates_id_patch_request_dict = shipping_rates_id_patch_request_instance.to_dict()
# create an instance of ShippingRatesIdPatchRequest from a dict
shipping_rates_id_patch_request_form_dict = shipping_rates_id_patch_request.from_dict(shipping_rates_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


