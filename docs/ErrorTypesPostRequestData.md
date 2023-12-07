# ErrorTypesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**ErrorTypes**](ErrorTypes.md) |  | [optional] 

## Example

```python
from webshipperv2.models.error_types_post_request_data import ErrorTypesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorTypesPostRequestData from a JSON string
error_types_post_request_data_instance = ErrorTypesPostRequestData.from_json(json)
# print the JSON string representation of the object
print ErrorTypesPostRequestData.to_json()

# convert the object into a dict
error_types_post_request_data_dict = error_types_post_request_data_instance.to_dict()
# create an instance of ErrorTypesPostRequestData from a dict
error_types_post_request_data_form_dict = error_types_post_request_data.from_dict(error_types_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


