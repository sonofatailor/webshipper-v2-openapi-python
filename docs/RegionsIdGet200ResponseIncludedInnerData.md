# RegionsIdGet200ResponseIncludedInnerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_id** | **int** | Id of the carrier which the shipping rate belongs to | [optional] [readonly] 
**order_channel_id** | **int** | Id of the order channel which the shipping rate belongs to | [optional] [readonly] 
**name** | **str** | Name to be displayed in the e-commerce system. | [optional] 
**carrier_service_code** | **str** | The carrier&#39;s service code which must be used when generating parcels with this shipping rate. | [optional] 
**require_drop_point** | **bool** | Determines if the shipping rate requires a drop point to be assigned. | [optional] 
**visible_for** | **int** | Enum - determines whether the rate is returned for all customers, private_customers or business customers. This must be one of the following values:  &lt;code&gt;any&lt;/code&gt;, &lt;code&gt;privat_customers&lt;/code&gt;, &lt;code&gt;business_customers&lt;/code&gt; | [optional] 
**service_attributes** | **str** | Array of flattened resources of type &lt;code&gt;Service Attribute&lt;/code&gt;. Depends on the carrier service&#39;s requirements. Service Attribute has the following attributes:  &lt;code&gt;attr_key&lt;/code&gt;, &lt;code&gt;attr_value&lt;/code&gt;. You may use the Webshipper Template Language (WTL) for the values. | [optional] 
**dimensions** | **str** | Predefined dimensions which are a assigned when using the shipping rate. Attributes are: &lt;code&gt;height&lt;/code&gt;,&lt;code&gt;width&lt;/code&gt; and &lt;code&gt;length&lt;/code&gt;. The Webshipper Template Language (WTL) may be used for the values. | [optional] 
**add_ons** | **str** | Array of add_ons supported by the carrier service. | [optional] 
**is_return** | **bool** | Defines whether the rate is a return (inbound) rate or a standard rate (outbound). Please be aware that this attribute must match the carrier&#39;s service type. | [optional] 
**carriers_email** | **bool** | When this is set to true, the shipping rate will enable e-mail notifications from the carrier. | [optional] 
**comment_map** | **str** | Defines what content is included in the comment field. The Webshipper Template Language (WTL) may be used in this field. For example:  {{order.external_comment}} | [optional] 
**reference_map** | **str** | Defines what content is included in the reference field. The Webshipper Template Language (WTL) may be used in this field. For example: {{order.visible_ref}} | [optional] 
**carriers_sms** | **bool** | When this is set to true, the shipping rate will enable SMS notifications from the carrier. | [optional] 
**dutiable** | **bool** | Defines whether the goods sent using this shipping rate are dutiable. | [optional] 
**is_hidden** | **bool** | Attribute to indicate if the shipping rate is visible to order channels | [optional] 
**click_collect** | **bool** |  | [optional] 
**reference** | **str** |  | [optional] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**default_colli_type** | **str** | Predefined colli type to be used when using the shipping rate. Must be supported by the carrier. | [optional] 
**sender_address_id** | **int** |  | [optional] 
**return_address_id** | **int** |  | [optional] 
**invoice_settings** | **str** |  | [optional] 
**shadow_booking_keep_labels** | **bool** |  | [optional] 
**shadow_booking_keep_documents** | **bool** |  | [optional] 
**ignore_rate_quote_validation** | **bool** |  | [optional] 
**custom_message** | **str** | Custom message to be displayed for the shipping rate | [optional] 
**regions** | **str** | Flattended array of Regions. See section on Shipping Regions and Expressions for more details | [optional] 

## Example

```python
from webshipperv2.models.regions_id_get200_response_included_inner_data import RegionsIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of RegionsIdGet200ResponseIncludedInnerData from a JSON string
regions_id_get200_response_included_inner_data_instance = RegionsIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print RegionsIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
regions_id_get200_response_included_inner_data_dict = regions_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of RegionsIdGet200ResponseIncludedInnerData from a dict
regions_id_get200_response_included_inner_data_form_dict = regions_id_get200_response_included_inner_data.from_dict(regions_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


