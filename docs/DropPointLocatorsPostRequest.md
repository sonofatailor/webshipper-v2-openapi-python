# DropPointLocatorsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DropPointLocatorsPostRequestData**](DropPointLocatorsPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.drop_point_locators_post_request import DropPointLocatorsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DropPointLocatorsPostRequest from a JSON string
drop_point_locators_post_request_instance = DropPointLocatorsPostRequest.from_json(json)
# print the JSON string representation of the object
print DropPointLocatorsPostRequest.to_json()

# convert the object into a dict
drop_point_locators_post_request_dict = drop_point_locators_post_request_instance.to_dict()
# create an instance of DropPointLocatorsPostRequest from a dict
drop_point_locators_post_request_form_dict = drop_point_locators_post_request.from_dict(drop_point_locators_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


