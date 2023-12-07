# CsvMappings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**separator** | **str** | The seperator in the file. Normally &#39;;&#39; or &#39;,&#39; | [optional] 
**target_class** | **str** | Must be one of the models &lt;code&gt;Order&lt;/code&gt; or &lt;code&gt;Shipment&lt;/code&gt; | [optional] 
**grouped_by** | **int** | Must be the index of the Order ID | [optional] 
**grouped_path** | **str** | The sub-model which you are grouping. For order: order_lines_attributes | [optional] 
**includes_header** | **bool** | Determines if there is an ignorable header line in the file | [optional] 
**lines_as_package** | **bool** |  | [optional] 
**recreate_order_lines** | **bool** |  | [optional] 
**separate_order_line_mapping** | **bool** |  | [optional] 
**name** | **str** | Name of the configuration | [optional] 
**example_input** | **str** | Example input to make it easier to create the mapping in the UI. | [optional] 
**line_example_input** | **str** |  | [optional] 
**rules** | **List[str]** | Array of flattened resources of the type CSV Rule | [optional] 
**shipment_export_format** | **str** |  | [optional] 
**order_export_format** | **str** |  | [optional] 
**create_shipment_automatically** | **bool** |  | [optional] 
**force_async** | **bool** |  | [optional] 
**concat_paths** | **bool** |  | [optional] 
**split_large_records** | **bool** |  | [optional] 
**export_file_extension** | **str** |  | [optional] 

## Example

```python
from webshipperv2.models.csv_mappings import CsvMappings

# TODO update the JSON string below
json = "{}"
# create an instance of CsvMappings from a JSON string
csv_mappings_instance = CsvMappings.from_json(json)
# print the JSON string representation of the object
print CsvMappings.to_json()

# convert the object into a dict
csv_mappings_dict = csv_mappings_instance.to_dict()
# create an instance of CsvMappings from a dict
csv_mappings_form_dict = csv_mappings.from_dict(csv_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


