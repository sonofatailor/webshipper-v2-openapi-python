# CarrierTypes


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

## Example

```python
from webshipperv2.models.carrier_types import CarrierTypes

# TODO update the JSON string below
json = "{}"
# create an instance of CarrierTypes from a JSON string
carrier_types_instance = CarrierTypes.from_json(json)
# print the JSON string representation of the object
print CarrierTypes.to_json()

# convert the object into a dict
carrier_types_dict = carrier_types_instance.to_dict()
# create an instance of CarrierTypes from a dict
carrier_types_form_dict = carrier_types.from_dict(carrier_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


