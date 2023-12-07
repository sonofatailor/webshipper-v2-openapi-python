# DropPointLocators


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_id** | **int** | ID of the carrier that you want to quote. &lt;strong&gt;This is only mandatory if no shipping_rate_id is given&lt;/strong&gt;. | [optional] 
**service_code** | **str** | Service code for the service that you want to quote. &lt;strong&gt;This is only mandatory if no shipping_rate_id is given.&lt;/strong&gt; | [optional] 
**shipping_rate_id** | **str** | ID of the shipping rate that you want to quote. &lt;strong&gt;This is only mandatory if no carrier_id is given.&lt;/strong&gt;. | [optional] 
**drop_point_id** | **str** |  | [optional] 
**delivery_address** | **str** | Flattened shipping address object. &lt;code&gt;zip&lt;/code&gt; and &lt;code&gt;country_code&lt;/code&gt;  are required and &lt;code&gt;address_1&lt;/code&gt; is optional. | [optional] 
**drop_points** | [**List[DropPoints]**](DropPoints.md) | Array of drop points near delivery_address. This will be populated in the response. | [optional] 

## Example

```python
from openapi_client.models.drop_point_locators import DropPointLocators

# TODO update the JSON string below
json = "{}"
# create an instance of DropPointLocators from a JSON string
drop_point_locators_instance = DropPointLocators.from_json(json)
# print the JSON string representation of the object
print DropPointLocators.to_json()

# convert the object into a dict
drop_point_locators_dict = drop_point_locators_instance.to_dict()
# create an instance of DropPointLocators from a dict
drop_point_locators_form_dict = drop_point_locators.from_dict(drop_point_locators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


