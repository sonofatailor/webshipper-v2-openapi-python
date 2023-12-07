# Waybills


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**waybill_name** | **str** | Name of the waybill type | [optional] 
**waybill_code** | **str** | Code identifying the type of waybill | [optional] 
**reference** | **str** | Unique reference returned from the carrier implementation when a waybill is opened. | [optional] 
**consolidation_key** | **str** |  | [optional] 
**barcode_serial** | **int** | This will be assigned by the API if the waybill type has a barcode requirement. | [optional] 
**status** | **int** | Indicates whether the waybill is open or closed. When you want to close the waybill, you simply need to update the status of the way bill and set it to closed. | [optional] 
**shipment_count** | **str** | This is a read-only attribute which returns the total number of shipments. | [optional] 
**currency** | **str** |  | [optional] 
**copies** | **int** |  | [optional] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**documents** | **str** | Array of documents. This is available when the waybill is closed. | [optional] 

## Example

```python
from webshipperv2.models.waybills import Waybills

# TODO update the JSON string below
json = "{}"
# create an instance of Waybills from a JSON string
waybills_instance = Waybills.from_json(json)
# print the JSON string representation of the object
print Waybills.to_json()

# convert the object into a dict
waybills_dict = waybills_instance.to_dict()
# create an instance of Waybills from a dict
waybills_form_dict = waybills.from_dict(waybills_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


