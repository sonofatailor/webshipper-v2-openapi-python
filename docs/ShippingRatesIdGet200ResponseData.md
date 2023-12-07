# ShippingRatesIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**ShippingRates**](ShippingRates.md) |  | [optional] 

## Example

```python
from webshipperv2.models.shipping_rates_id_get200_response_data import ShippingRatesIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingRatesIdGet200ResponseData from a JSON string
shipping_rates_id_get200_response_data_instance = ShippingRatesIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print ShippingRatesIdGet200ResponseData.to_json()

# convert the object into a dict
shipping_rates_id_get200_response_data_dict = shipping_rates_id_get200_response_data_instance.to_dict()
# create an instance of ShippingRatesIdGet200ResponseData from a dict
shipping_rates_id_get200_response_data_form_dict = shipping_rates_id_get200_response_data.from_dict(shipping_rates_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


