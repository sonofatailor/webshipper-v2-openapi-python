# Carriers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Your name for the carrier | [optional] 
**services** | **str** | Array of services provided by this Carrier | [optional] 
**attrs** | **str** | Array of hashes with keys: &lt;code&gt;attr_key&lt;/code&gt;, &lt;code&gt;attr_value&lt;/code&gt;, &lt;code&gt;attr_name&lt;/code&gt;, &lt;code&gt;attr_type&lt;/code&gt;, &lt;code&gt;is_required&lt;/code&gt;, &lt;code&gt;only_visible_on_creation&lt;/code&gt;, &lt;/code&gt;enums&lt;/code&gt;. See       documentation for Local Attributes | [optional] 
**prefer_zpl** | **bool** |  | [optional] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**is_approved** | **bool** |  | [optional] 
**approved_service_codes** | **str** |  | [optional] 
**service_parameter_enums** | **str** |  | [optional] 
**barcode_notification_behavior** | **int** |  | [optional] 
**barcode_notification_mail** | **str** |  | [optional] 
**has_active_cost_sheet** | **str** |  | [optional] 
**delete_at_carrier** | **bool** |  | [optional] 
**test_mode** | **bool** |  | [optional] 
**logo** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**print_error_label** | **bool** |  | [optional] 
**ftp_configuration_id** | **int** |  | [optional] 

## Example

```python
from webshipperv2.models.carriers import Carriers

# TODO update the JSON string below
json = "{}"
# create an instance of Carriers from a JSON string
carriers_instance = Carriers.from_json(json)
# print the JSON string representation of the object
print Carriers.to_json()

# convert the object into a dict
carriers_dict = carriers_instance.to_dict()
# create an instance of Carriers from a dict
carriers_form_dict = carriers.from_dict(carriers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


