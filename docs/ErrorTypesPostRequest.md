# ErrorTypesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ErrorTypesPostRequestData**](ErrorTypesPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.error_types_post_request import ErrorTypesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorTypesPostRequest from a JSON string
error_types_post_request_instance = ErrorTypesPostRequest.from_json(json)
# print the JSON string representation of the object
print ErrorTypesPostRequest.to_json()

# convert the object into a dict
error_types_post_request_dict = error_types_post_request_instance.to_dict()
# create an instance of ErrorTypesPostRequest from a dict
error_types_post_request_form_dict = error_types_post_request.from_dict(error_types_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


