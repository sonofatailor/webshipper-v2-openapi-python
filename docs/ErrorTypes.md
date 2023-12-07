# ErrorTypes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**translations** | **str** |  | [optional] 
**matcher** | **str** |  | [optional] 
**error_class** | **str** |  | [optional] 
**support_url** | **str** |  | [optional] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 

## Example

```python
from openapi_client.models.error_types import ErrorTypes

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorTypes from a JSON string
error_types_instance = ErrorTypes.from_json(json)
# print the JSON string representation of the object
print ErrorTypes.to_json()

# convert the object into a dict
error_types_dict = error_types_instance.to_dict()
# create an instance of ErrorTypes from a dict
error_types_form_dict = error_types.from_dict(error_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


