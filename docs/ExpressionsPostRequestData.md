# ExpressionsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Expressions**](Expressions.md) |  | [optional] 

## Example

```python
from openapi_client.models.expressions_post_request_data import ExpressionsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ExpressionsPostRequestData from a JSON string
expressions_post_request_data_instance = ExpressionsPostRequestData.from_json(json)
# print the JSON string representation of the object
print ExpressionsPostRequestData.to_json()

# convert the object into a dict
expressions_post_request_data_dict = expressions_post_request_data_instance.to_dict()
# create an instance of ExpressionsPostRequestData from a dict
expressions_post_request_data_form_dict = expressions_post_request_data.from_dict(expressions_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


