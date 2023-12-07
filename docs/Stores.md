# Stores


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**address_1** | **str** |  | [optional] 
**address_2** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**longitude** | **str** |  | [optional] 
**latitude** | **str** |  | [optional] 

## Example

```python
from webshipperv2.models.stores import Stores

# TODO update the JSON string below
json = "{}"
# create an instance of Stores from a JSON string
stores_instance = Stores.from_json(json)
# print the JSON string representation of the object
print Stores.to_json()

# convert the object into a dict
stores_dict = stores_instance.to_dict()
# create an instance of Stores from a dict
stores_form_dict = stores.from_dict(stores_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


