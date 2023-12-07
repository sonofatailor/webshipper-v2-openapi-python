# ReportTypes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**columns** | **List[str]** | Array of objects with keys &lt;code&gt;header&lt;/code&gt; and &lt;code&gt;content&lt;/code&gt; | [optional] 
**parameters** | **List[str]** | Array of objects with keys &lt;code&gt;parameter_key&lt;/code&gt; and &lt;code&gt;parameter_value&lt;/code&gt; | [optional] 
**resource** | **str** |  | [optional] 
**header_columns** | **List[str]** | Array of objects with keys &lt;code&gt;header&lt;/code&gt; and &lt;code&gt;content&lt;/code&gt; that will be used to display the header content of the report | [optional] 
**footer_content** | **str** |  | [optional] 
**conditions** | **List[str]** | Array of objects describing how to load the resources. Contains keys &lt;code&gt;condition_key&lt;/code&gt;, &lt;code&gt;condition_operator&lt;/code&gt;, &lt;code&gt;condition_value&lt;/code&gt;. | [optional] 
**include_deleted** | **bool** | If true the report will included deleted records. Default: &lt;code&gt;false&lt;/code&gt; | [optional] 
**use_carrier_eod** | **bool** | When set to true it will attempt to fetch the end of day list directly from the carrier. When this option is enabled, only pdf reports are available. | [optional] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**schedule** | **str** |  | [optional] 
**default_format** | **str** |  | [optional] 
**mail_on_run** | **bool** |  | [optional] 
**mail** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.report_types import ReportTypes

# TODO update the JSON string below
json = "{}"
# create an instance of ReportTypes from a JSON string
report_types_instance = ReportTypes.from_json(json)
# print the JSON string representation of the object
print ReportTypes.to_json()

# convert the object into a dict
report_types_dict = report_types_instance.to_dict()
# create an instance of ReportTypes from a dict
report_types_form_dict = report_types.from_dict(report_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


