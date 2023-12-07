# AdditionalAttributesIdGet200ResponseIncludedInnerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_channel_id** | **int** | DEPRECATED Assign a relation instead | [optional] 
**status** | **int** | Possible enum values: pending, dispatched or returned | [optional] 
**ext_ref** | **str** | External reference of the order line. | [optional] 
**visible_ref** | **str** | Visible reference - the friendly/visible external order number | [optional] 
**drop_point** | [**DropPoints**](DropPoints.md) |  | [optional] 
**original_shipping** | **object** | Flattened resource describing the original shipping option from the order channel. This will be used for matching in cases where shipping was not quoted from Webshipper. | [optional] 
**order_lines** | [**List[OrderLines]**](OrderLines.md) | Flattened resource of type OrderLine | [optional] 
**delivery_address** | [**ShippingAddresses**](ShippingAddresses.md) |  | [optional] 
**sender_address** | [**ShippingAddresses**](ShippingAddresses.md) |  | [optional] 
**billing_address** | [**ShippingAddresses**](ShippingAddresses.md) |  | [optional] 
**sold_from_address** | [**ShippingAddresses**](ShippingAddresses.md) |  | [optional] 
**currency** | **str** | Currency code of the order | [optional] 
**internal_comment** | **str** | Latest comment with type &#39;internal&#39;. Changing this, will create a new comment | [optional] 
**external_comment** | **str** | External order comment. Will typically be the order comment from e-commerce checkout. | [optional] 
**error_message** | **object** | Any error message that resulted from the latest attempt at making a shipment from the order. | [optional] 
**slip** | **str** | The order slip in PDF format using base64 encoding. This will only be included if the parameter fields[orders] includes slip. | [optional] [readonly] 
**var_base64** | **str** |  | [optional] [readonly] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**lock_state** | **str** | When an order is locked, it cannot be modified or sent until it is unlocked. Possible values: &lt;code&gt;locked&lt;/code&gt; or &lt;code&gt;unlocked&lt;/code&gt;. | [optional] 
**source** | **str** | A description of how the order was created in Webshipper. Possible values: &#39;api&#39;, &#39;manual&#39; or &#39;csv&#39; | [optional] 
**tags** | **List[str]** | Array of strings used to tag an order | [optional] 
**error_class** | **str** | A string like &#39;address&#39; or &#39;carrier_downtime&#39; describe which type of error caused the order to fail | [optional] 
**slip_printed** | **bool** |  | [optional] 
**label_printed** | **bool** |  | [optional] 
**create_shipment_automatically** | **str** |  | [optional] 
**latest_activity** | **str** |  | [optional] 
**latest_status_event** | **str** |  | [optional] 
**shipping_rate_id** | **int** |  | [optional] 
**csv_upload_id** | **int** |  | [optional] 
**sku** | **str** | Stock Keeping Unit of the order line | [optional] 
**description** | **str** | Description of the goods | [optional] 
**quantity** | **int** | Quantity of goods | [optional] 
**location** | **str** | The warehouse location of the items. | [optional] 
**tarif_number** | **str** | HS Tarif code for paperless customs | [optional] 
**country_of_origin** | **str** | The country of origin of the goods. | [optional] 
**unit_price** | **float** | The unit price of goods in the currency of the order | [optional] 
**package_id** | **int** | Whether the items are associated with a parcel of a shipment. | [optional] 
**discounted_unit_price** | **str** | The unit price after discounts has been applied in the currency of the order | [optional] 
**discount_value** | **float** | The discount for the order line, in the type given by discount_type | [optional] 
**discount_type** | **int** | The type of discount, eg. percent or fixed | [optional] 
**vat_percent** | **float** | The VAT rate in percentage. | [optional] 
**order_id** | **int** |  | [optional] 
**weight** | **float** | Weight per unit. | [optional] 
**weight_unit** | **str** | Weight unit. Possible values: &lt;code&gt;oz&lt;/code&gt;, &lt;code&gt;g&lt;/code&gt;, &lt;code&gt;lbs&lt;/code&gt;, &lt;code&gt;kg&lt;/code&gt;. Defaults to &lt;code&gt;g&lt;/code&gt; | [optional] 
**is_virtual** | **bool** |  | [optional] 
**dangerous_goods_details** | **object** | Optional object of key value pairs used for providing information of dangerous goods. For use with DGOffice, use keys: article_no, package_type_id and packaging_instruction_type. | [optional] 

## Example

```python
from openapi_client.models.additional_attributes_id_get200_response_included_inner_data import AdditionalAttributesIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalAttributesIdGet200ResponseIncludedInnerData from a JSON string
additional_attributes_id_get200_response_included_inner_data_instance = AdditionalAttributesIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print AdditionalAttributesIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
additional_attributes_id_get200_response_included_inner_data_dict = additional_attributes_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of AdditionalAttributesIdGet200ResponseIncludedInnerData from a dict
additional_attributes_id_get200_response_included_inner_data_form_dict = additional_attributes_id_get200_response_included_inner_data.from_dict(additional_attributes_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


