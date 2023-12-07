# CarrierAccesses


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 

## Example

```python
from webshipperv2.models.carrier_accesses import CarrierAccesses

# TODO update the JSON string below
json = "{}"
# create an instance of CarrierAccesses from a JSON string
carrier_accesses_instance = CarrierAccesses.from_json(json)
# print the JSON string representation of the object
print CarrierAccesses.to_json()

# convert the object into a dict
carrier_accesses_dict = carrier_accesses_instance.to_dict()
# create an instance of CarrierAccesses from a dict
carrier_accesses_form_dict = carrier_accesses.from_dict(carrier_accesses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


