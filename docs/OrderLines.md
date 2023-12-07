# OrderLines


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**status** | **int** | Possible enum values: pending, dispatched or returned | [optional] 
**ext_ref** | **str** | External reference of the order line. | [optional] 
**weight** | **float** | Weight per unit. | [optional] 
**weight_unit** | **str** | Weight unit. Possible values: &lt;code&gt;oz&lt;/code&gt;, &lt;code&gt;g&lt;/code&gt;, &lt;code&gt;lbs&lt;/code&gt;, &lt;code&gt;kg&lt;/code&gt;. Defaults to &lt;code&gt;g&lt;/code&gt; | [optional] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**is_virtual** | **bool** |  | [optional] 
**dangerous_goods_details** | **object** | Optional object of key value pairs used for providing information of dangerous goods. For use with DGOffice, use keys: article_no, package_type_id and packaging_instruction_type. | [optional] 

## Example

```python
from webshipperv2.models.order_lines import OrderLines

# TODO update the JSON string below
json = "{}"
# create an instance of OrderLines from a JSON string
order_lines_instance = OrderLines.from_json(json)
# print the JSON string representation of the object
print OrderLines.to_json()

# convert the object into a dict
order_lines_dict = order_lines_instance.to_dict()
# create an instance of OrderLines from a dict
order_lines_form_dict = order_lines.from_dict(order_lines_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


