# DropPointLocatorsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**DropPointLocators**](DropPointLocators.md) |  | [optional] 

## Example

```python
from openapi_client.models.drop_point_locators_post_request_data import DropPointLocatorsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of DropPointLocatorsPostRequestData from a JSON string
drop_point_locators_post_request_data_instance = DropPointLocatorsPostRequestData.from_json(json)
# print the JSON string representation of the object
print DropPointLocatorsPostRequestData.to_json()

# convert the object into a dict
drop_point_locators_post_request_data_dict = drop_point_locators_post_request_data_instance.to_dict()
# create an instance of DropPointLocatorsPostRequestData from a dict
drop_point_locators_post_request_data_form_dict = drop_point_locators_post_request_data.from_dict(drop_point_locators_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


