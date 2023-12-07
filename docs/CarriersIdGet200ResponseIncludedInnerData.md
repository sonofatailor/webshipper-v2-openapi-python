# CarriersIdGet200ResponseIncludedInnerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fulfillment_logo** | **str** | Logo for the carrier | [optional] 
**list_logo** | **str** | Logo for the carrier | [optional] 
**name** | **str** | Name of the carrier | [optional] 
**carrier_code** | **str** | Code identifying the carrier | [optional] 
**description** | **str** | Description of the carrier | [optional] 
**required_details** | **str** | Details required to use the carrier | [optional] 
**requires_dutiable** | **bool** |  | [optional] 
**supports_zpl** | **bool** |  | [optional] 
**supports_pickup** | **str** |  | [optional] 
**supports_tracking** | **str** |  | [optional] 
**supports_price_quoting** | **bool** |  | [optional] 
**requires_approval** | **bool** |  | [optional] 
**supports_documents** | **bool** |  | [optional] 
**supports_shipment_updates** | **bool** | Boolean indicating wether the carrier supports shipment updates | [optional] 
**shipment_updates_limit_minutes** | **int** | Number of minutes before shipment time a shipment can be updated | [optional] 
**barcode_mail** | **str** |  | [optional] 
**supports_price_pdf_upload** | **str** |  | [optional] 
**supports_deletion** | **str** |  | [optional] 
**barcode_customer_notification_mail_template_id** | **int** |  | [optional] 
**colli_type_support** | **int** | Determines whether the carrier supports colli types.Values should be one of the following. null: Not supported, \&quot;carrier_provided\&quot;: Values are determined by the carrier, \&quot;webshipper_provided\&quot;: Default Webshipper colli types, \&quot;customer_provided\&quot;: The customer can input colli types specific to their aggreement with the carrier. | [optional] 
**beta** | **bool** |  | [optional] 
**supports_test_mode** | **bool** |  | [optional] 
**show_send_time** | **bool** |  | [optional] 
**supports_shadow_bookings** | **bool** |  | [optional] 
**rate_quote_validation** | **bool** |  | [optional] 
**carrier_group_id** | **str** |  | [optional] 
**require_ftp_configuration_id** | **bool** |  | [optional] 
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
from webshipperv2.models.carriers_id_get200_response_included_inner_data import CarriersIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of CarriersIdGet200ResponseIncludedInnerData from a JSON string
carriers_id_get200_response_included_inner_data_instance = CarriersIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print CarriersIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
carriers_id_get200_response_included_inner_data_dict = carriers_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of CarriersIdGet200ResponseIncludedInnerData from a dict
carriers_id_get200_response_included_inner_data_form_dict = carriers_id_get200_response_included_inner_data.from_dict(carriers_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


