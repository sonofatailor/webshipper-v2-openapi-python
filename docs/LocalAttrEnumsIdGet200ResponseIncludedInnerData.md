# LocalAttrEnumsIdGet200ResponseIncludedInnerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr_name** | **str** | Visible name of the attribute | [optional] 
**attr_key** | **str** | Key for the attribute. Used by the system to read the correct information | [optional] 
**attr_type** | **str** | Data type. Must be either of the following: &lt;code&gt;string&lt;/code&gt;, &lt;code&gt;integer&lt;/code&gt; or &lt;code&gt;password&lt;/code&gt; | [optional] 
**is_required** | **bool** | Determines if the form should require the attr to be filled | [optional] 
**description** | **str** | Help text to describe the attribute | [optional] 
**requirement_type** | **int** |  | [optional] 
**category** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 
**only_visible_on_creation** | **bool** | Determines if the form should only be visible when connecting | [optional] 

## Example

```python
from openapi_client.models.local_attr_enums_id_get200_response_included_inner_data import LocalAttrEnumsIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of LocalAttrEnumsIdGet200ResponseIncludedInnerData from a JSON string
local_attr_enums_id_get200_response_included_inner_data_instance = LocalAttrEnumsIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print LocalAttrEnumsIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
local_attr_enums_id_get200_response_included_inner_data_dict = local_attr_enums_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of LocalAttrEnumsIdGet200ResponseIncludedInnerData from a dict
local_attr_enums_id_get200_response_included_inner_data_form_dict = local_attr_enums_id_get200_response_included_inner_data.from_dict(local_attr_enums_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


