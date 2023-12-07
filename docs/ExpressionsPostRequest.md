# ExpressionsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ExpressionsPostRequestData**](ExpressionsPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.expressions_post_request import ExpressionsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExpressionsPostRequest from a JSON string
expressions_post_request_instance = ExpressionsPostRequest.from_json(json)
# print the JSON string representation of the object
print ExpressionsPostRequest.to_json()

# convert the object into a dict
expressions_post_request_dict = expressions_post_request_instance.to_dict()
# create an instance of ExpressionsPostRequest from a dict
expressions_post_request_form_dict = expressions_post_request.from_dict(expressions_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


