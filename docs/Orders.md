# Orders


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_channel_id** | **int** | DEPRECATED Assign a relation instead | [optional] 
**status** | **str** | Enum status of the order. Possible values: pending, dispatched, partly_dispatched, cancelled, error, missing_rate, on_hold | [optional] 
**ext_ref** | **str** | External ( hidden ) reference for the order. Used by system to update the order in e.g. order channels. Must be unique in scope of order channels. | [optional] 
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

## Example

```python
from openapi_client.models.orders import Orders

# TODO update the JSON string below
json = "{}"
# create an instance of Orders from a JSON string
orders_instance = Orders.from_json(json)
# print the JSON string representation of the object
print Orders.to_json()

# convert the object into a dict
orders_dict = orders_instance.to_dict()
# create an instance of Orders from a dict
orders_form_dict = orders.from_dict(orders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


