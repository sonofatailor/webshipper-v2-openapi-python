# SlipTemplates


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name to identify the template. | [optional] 
**slip_size** | **int** | Size of the parcel slip. Possible values: &lt;code&gt;A4&lt;/code&gt; and &lt;code&gt;4X6&lt;/code&gt; | [optional] 
**additional_content** | **str** | Content after the table of order lines for A4-based parcel slips. | [optional] 
**additional_content_align** | **int** | Alignment of additional_content. Possible values: &lt;code&gt;center&lt;/code&gt;, &lt;code&gt;right&lt;/code&gt;, &lt;code&gt;left&lt;/code&gt; | [optional] 
**barcode_content** | **str** | Content of the barcode | [optional] 
**header_content** | **str** | Content of the slip header | [optional] 
**top_left_content_header** | **str** | Header of the top left corner | [optional] 
**top_right_content_header** | **str** | Header of the top right corner | [optional] 
**top_left_content** | **str** | Content of the top left corner | [optional] 
**top_right_content** | **str** | Content of the top right corner | [optional] 
**footer_content** | **str** | Content of the footer | [optional] 
**slip_template_columns** | **str** | Array of columns. Column objects contains: &lt;code&gt;name&lt;/code&gt;&lt;code&gt;content&lt;/code&gt;, &lt;code&gt;text_alignment&lt;/code&gt;(right, left, center), &lt;code&gt;width&lt;/code&gt; (in percentage) | [optional] 
**table_color** | **str** | HEX color including # | [optional] 
**table_text_color** | **str** | HEX color including # | [optional] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**sort_key** | **str** | The key to sort the order-lines by | [optional] 
**returns_only** | **bool** |  | [optional] 
**disable_inline_formatting** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.slip_templates import SlipTemplates

# TODO update the JSON string below
json = "{}"
# create an instance of SlipTemplates from a JSON string
slip_templates_instance = SlipTemplates.from_json(json)
# print the JSON string representation of the object
print SlipTemplates.to_json()

# convert the object into a dict
slip_templates_dict = slip_templates_instance.to_dict()
# create an instance of SlipTemplates from a dict
slip_templates_form_dict = slip_templates.from_dict(slip_templates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


