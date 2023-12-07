# CustomsLines


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | Stock Keeping Unit | [optional] 
**description** | **str** | Goods description | [optional] 
**quantity** | **int** | Quantity of the customs line | [optional] 
**tarif_number** | **str** | Tariff number / HS code | [optional] 
**country_of_origin** | **str** | Country of origin of the customs line - ISO 3166-1 alpha-2 | [optional] 
**unit_price** | **float** | Unit price of a single quantity customs line | [optional] 
**vat_percent** | **float** | Vat percent of the customs line | [optional] 
**currency** | **str** | Currency ISO-4217 | [optional] 
**weight** | **float** | Weight of a single quantity customs line | [optional] 
**weight_unit** | **int** | Weight unit of the customs line - One of &#39;g&#39;, &#39;oz&#39;, &#39;lbs&#39; or &#39;kg&#39; | [optional] 
**discount** | **float** | Discount of a single quantity customs line | [optional] 
**dangerous_goods_details** | **object** | Optional object of key value pairs used for providing information of dangerous goods. For use with DGOffice, use keys: article_no, package_type_id and packaging_instruction_type. | [optional] 

## Example

```python
from openapi_client.models.customs_lines import CustomsLines

# TODO update the JSON string below
json = "{}"
# create an instance of CustomsLines from a JSON string
customs_lines_instance = CustomsLines.from_json(json)
# print the JSON string representation of the object
print CustomsLines.to_json()

# convert the object into a dict
customs_lines_dict = customs_lines_instance.to_dict()
# create an instance of CustomsLines from a dict
customs_lines_form_dict = customs_lines.from_dict(customs_lines_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


