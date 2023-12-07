# Shipments


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | The reference you want to identify the shipment form. For example order number. | [optional] 
**comment** | **str** | An optional comment for the carrier | [optional] 
**service_code** | **str** | The carrier&#39;s service code. This should only be assigned if you are not using a shipping rate. | [optional] 
**is_return** | **bool** | Determines whether the shipment is a return shipment. | [optional] 
**packages** | [**List[Packages]**](Packages.md) | Flattened array of packages to be sent. At least one package is mandatory. For structure refer to &#39;Package&#39; entity | [optional] 
**delivery_address** | **object** | Flattened Shipping Address representing the delivery address for the shipment. &lt;br&gt;&lt;strong&gt;Duplicated from order if order relation given.&lt;/strong&gt;. | [optional] 
**sender_address** | **object** | Flattened Shipping Address representing the sender address of shipment. &lt;br&gt;&lt;strong&gt;Duplicated from order if order relation given.&lt;/strong&gt;. | [optional] 
**billing_address** | **object** | Flattened Shipping Address representing the billing address of shipment. Duplicated from delivery address if empty. &lt;br&gt;&lt;strong&gt;Duplicated from order if order relation given.&lt;/strong&gt;. | [optional] 
**pickup_address** | **object** | Flattened Shipping Address representing the pickup address of shipment. Is necessary for some carriers. This is duplicated from sender address if empty. &lt;br&gt;&lt;strong&gt;Duplicated from order if order relation given.&lt;/strong&gt;. | [optional] 
**return_address** | **object** | Flattened Shipping Address represnting return addres of shipment. Will be duplicated from sender address if empty ( Not used by all carriers ). &lt;br&gt;&lt;strong&gt;Duplicated from order if order relation given.&lt;/strong&gt;. | [optional] 
**service_attributes** | **List[str]** | Array of hashes to assign parameters for any specific carrier service. It is only required if you are &lt;strong&gt;not&lt;/strong&gt; using shipping rates and the service has additional required parameters. The hash must have the keys attr_key and attr_value. The type of attr_value should match the attr_type defined by the parameter. To see all possible attributes, please see the list of parameters from the carrier service. &lt;strongShould only be assigned if you are not using a shipping rate&lt;/strong&gt;. | [optional] 
**add_ons** | **List[str]** | Array of add-ons. Add-ons are simply arrays of strings. To see possible add-ons, please refer to the carrier services. &lt;strong&gt;Should only be assigned if you are not using a shipping rate&lt;/strong&gt;. | [optional] 
**sms_notification** | **str** | Must be passed if the carrier should be allowed to send SMS notifications. It should be assigned with a hash including the key phone containing the phone number to be notified. &lt;strong&gt;Should only be assigned if you are not using a shipping rate&lt;/strong&gt;. | [optional] 
**email_notification** | **str** | Must be passed if the carrier should be allowed to send e-mail notifications. It should be assigned with a hash including the key email containing the e-mail address to be notified. &lt;strong&gt;Should only be assigned if you are not using a shipping rate&lt;/strong&gt;. | [optional] 
**included_documents** | **str** | Flattened array of Document - can be used to upload documents to the shipment which will be sent to the carrier. | [optional] 
**drop_point** | **str** | Flattened Drop Point - should only be assigned if you are sending to a drop point. | [optional] 
**tracking_links** | [**List[ShipmentsTrackingLinksInner]**](ShipmentsTrackingLinksInner.md) | An array of objects with the keys:       &lt;ul&gt;         &lt;li&gt;&lt;code&gt;url&lt;/code&gt;: The full URL to the tracking page.&lt;/li&gt;         &lt;li&gt;&lt;code&gt;number&lt;/code&gt;: The tracking identifier.&lt;/li&gt;         &lt;li&gt;&lt;code&gt;latest_transit_event&lt;/code&gt;: The latest tracking/transit event. Same options as Tracking Event statuses.&lt;/li&gt;         &lt;li&gt;&lt;code&gt;tracking_events&lt;/code&gt;: Array of objects. Object has same attributes as the Tracking Event resource&lt;/li&gt;       &lt;/ul&gt;        | [optional] 
**fulfill_immediately** | **str** | Deprecated | [optional] 
**test_mode** | **bool** |  | [optional] 
**dutiable** | **bool** |  | [optional] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**ext_ref** | **str** | The external (carrier) reference | [optional] 
**original_shipment_id** | **int** |  | [optional] 
**send_time** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**latest_update_time** | **str** |  | [optional] 
**supports_updates** | **str** |  | [optional] 
**additional_attributes** | **str** | Flattened hash with optional key/value pairs. | [optional] 
**cost_price** | **float** | The cost price of the shipment, either directly from the carrier or from a cost sheet | [optional] 
**sales_price** | **float** | The price presented to the customer in checkout | [optional] 
**currency** | **str** |  | [optional] 
**manual_order_shipment_creation** | **str** |  | [optional] 
**carrier_type_name** | **str** | Webshipper defined name of the carrier type | [optional] [readonly] 
**carrier_alias** | **str** | Carrier alias set by the user in Webshipper | [optional] [readonly] 
**carrier_id** | **int** | ID of the carrier | [optional] [readonly] 
**invoice_settings** | **str** |  | [optional] 
**latest_activity** | **str** |  | [optional] 
**latest_status_event** | **str** |  | [optional] 
**shadow_booking_as_parent** | **str** |  | [optional] 
**source** | **int** |  | [optional] 
**document_template** | **str** |  | [optional] 
**csv_upload_id** | **int** |  | [optional] 
**omit_print** | **bool** |  | [optional] 
**original_shipment** | **str** | An optional link to the original shipment, when creating a return-shipment | [optional] 

## Example

```python
from webshipperv2.models.shipments import Shipments

# TODO update the JSON string below
json = "{}"
# create an instance of Shipments from a JSON string
shipments_instance = Shipments.from_json(json)
# print the JSON string representation of the object
print Shipments.to_json()

# convert the object into a dict
shipments_dict = shipments_instance.to_dict()
# create an instance of Shipments from a dict
shipments_form_dict = shipments.from_dict(shipments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


