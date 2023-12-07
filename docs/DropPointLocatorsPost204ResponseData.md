# DropPointLocatorsPost204ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**DropPointLocators**](DropPointLocators.md) |  | [optional] 

## Example

```python
from webshipperv2.models.drop_point_locators_post204_response_data import DropPointLocatorsPost204ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DropPointLocatorsPost204ResponseData from a JSON string
drop_point_locators_post204_response_data_instance = DropPointLocatorsPost204ResponseData.from_json(json)
# print the JSON string representation of the object
print DropPointLocatorsPost204ResponseData.to_json()

# convert the object into a dict
drop_point_locators_post204_response_data_dict = drop_point_locators_post204_response_data_instance.to_dict()
# create an instance of DropPointLocatorsPost204ResponseData from a dict
drop_point_locators_post204_response_data_form_dict = drop_point_locators_post204_response_data.from_dict(drop_point_locators_post204_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


