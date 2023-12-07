# Pickups


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_instruction** | **str** | Instruction to the carrier. | [optional] 
**pickup_location_close_time** | **str** | When the pickup location is closing. | [optional] 
**pickup_time** | **str** | The time you want the carrier to arrive at the pickup address. | [optional] 
**reference** | **str** | The reference returned by the carrier. | [optional] 
**status** | **int** | Decides if the pickup is &lt;code&gt;requested&lt;/code&gt; or &lt;code&gt;cancelled&lt;/code&gt;. To cancel a pickup you must update the status to cancelled.  | [optional] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**shipping_address** | **str** | The address where the shipments must be picked up. | [optional] 
**carrier** | **str** | The carrier that should pickup the shipments. | [optional] 

## Example

```python
from openapi_client.models.pickups import Pickups

# TODO update the JSON string below
json = "{}"
# create an instance of Pickups from a JSON string
pickups_instance = Pickups.from_json(json)
# print the JSON string representation of the object
print Pickups.to_json()

# convert the object into a dict
pickups_dict = pickups_instance.to_dict()
# create an instance of Pickups from a dict
pickups_form_dict = pickups.from_dict(pickups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


