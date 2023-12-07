# CustomsLinesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**CustomsLines**](CustomsLines.md) |  | [optional] 

## Example

```python
from openapi_client.models.customs_lines_post_request_data import CustomsLinesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CustomsLinesPostRequestData from a JSON string
customs_lines_post_request_data_instance = CustomsLinesPostRequestData.from_json(json)
# print the JSON string representation of the object
print CustomsLinesPostRequestData.to_json()

# convert the object into a dict
customs_lines_post_request_data_dict = customs_lines_post_request_data_instance.to_dict()
# create an instance of CustomsLinesPostRequestData from a dict
customs_lines_post_request_data_form_dict = customs_lines_post_request_data.from_dict(customs_lines_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


