# DropPointLocatorsPost204Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DropPointLocatorsPost204ResponseData**](DropPointLocatorsPost204ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.drop_point_locators_post204_response import DropPointLocatorsPost204Response

# TODO update the JSON string below
json = "{}"
# create an instance of DropPointLocatorsPost204Response from a JSON string
drop_point_locators_post204_response_instance = DropPointLocatorsPost204Response.from_json(json)
# print the JSON string representation of the object
print DropPointLocatorsPost204Response.to_json()

# convert the object into a dict
drop_point_locators_post204_response_dict = drop_point_locators_post204_response_instance.to_dict()
# create an instance of DropPointLocatorsPost204Response from a dict
drop_point_locators_post204_response_form_dict = drop_point_locators_post204_response.from_dict(drop_point_locators_post204_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


