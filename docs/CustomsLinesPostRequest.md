# CustomsLinesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CustomsLinesPostRequestData**](CustomsLinesPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.customs_lines_post_request import CustomsLinesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomsLinesPostRequest from a JSON string
customs_lines_post_request_instance = CustomsLinesPostRequest.from_json(json)
# print the JSON string representation of the object
print CustomsLinesPostRequest.to_json()

# convert the object into a dict
customs_lines_post_request_dict = customs_lines_post_request_instance.to_dict()
# create an instance of CustomsLinesPostRequest from a dict
customs_lines_post_request_form_dict = customs_lines_post_request.from_dict(customs_lines_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


