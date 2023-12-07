# ShippingAddresses


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**att_contact** | **str** | Att person. To generate parcels either att_contact &lt;strong&gt;or&lt;/strong&gt; company_name is required | [optional] 
**company_name** | **str** | Company name. To generate parcels either att_contact &lt;strong&gt;or&lt;/strong&gt; company_name is required | [optional] 
**address_1** | **str** | Address line 1 | [optional] 
**address_2** | **str** | Address line 2 | [optional] 
**country_code** | **str** | ISO 3166-1 alpha-2 code | [optional] 
**state** | **str** | Sub-division of country, if applicable. State code. ISO 3166-2 alpha-2 | [optional] 
**phone** | **str** | Phone number of the entity. This can be used for SMS notifications. | [optional] 
**email** | **str** | E-mail address of the entity. This can be used for e-mail notifications. | [optional] 
**zip** | **str** | Postal code of the entity. This is required for most destination countries. | [optional] 
**city** | **str** | City of the entity. This is required for most destination countries. | [optional] 
**vat_no** | **str** | The VAT number of the entity. This is only required for address_type &lt;code&gt;sold_from&lt;/code&gt; | [optional] 
**address_type** | **str** | Used for special addresses for order channels. This will be one of the following: &lt;code&gt;recipient&lt;/code&gt;, &lt;code&gt;sender&lt;/code&gt;, &lt;code&gt;sold_from&lt;/code&gt;, &lt;code&gt;pickup&lt;/code&gt;, &lt;code&gt;return&lt;/code&gt;, &lt;code&gt;order_address&lt;/code&gt; | [optional] 
**ext_location** | **str** |  | [optional] 
**voec** | **str** |  | [optional] 
**eori** | **str** |  | [optional] 
**sprn** | **str** |  | [optional] 
**ioss** | **str** |  | [optional] 
**fda** | **str** |  | [optional] 
**duns** | **str** |  | [optional] 
**personal_customs_no** | **str** |  | [optional] 
**company_customs_numbers** | **str** |  | [optional] 

## Example

```python
from webshipperv2.models.shipping_addresses import ShippingAddresses

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingAddresses from a JSON string
shipping_addresses_instance = ShippingAddresses.from_json(json)
# print the JSON string representation of the object
print ShippingAddresses.to_json()

# convert the object into a dict
shipping_addresses_dict = shipping_addresses_instance.to_dict()
# create an instance of ShippingAddresses from a dict
shipping_addresses_form_dict = shipping_addresses.from_dict(shipping_addresses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


