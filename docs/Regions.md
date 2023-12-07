# Regions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | [optional] 
**expressions** | **str** | Flattened array of expressions. Please see section 8 for more details regarding expressions. | [optional] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**countries** | **str** |  | [optional] 

## Example

```python
from webshipperv2.models.regions import Regions

# TODO update the JSON string below
json = "{}"
# create an instance of Regions from a JSON string
regions_instance = Regions.from_json(json)
# print the JSON string representation of the object
print Regions.to_json()

# convert the object into a dict
regions_dict = regions_instance.to_dict()
# create an instance of Regions from a dict
regions_form_dict = regions.from_dict(regions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


