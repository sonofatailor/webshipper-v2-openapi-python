# PrintablesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PrintablesPostRequestData**](PrintablesPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.printables_post_request import PrintablesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrintablesPostRequest from a JSON string
printables_post_request_instance = PrintablesPostRequest.from_json(json)
# print the JSON string representation of the object
print PrintablesPostRequest.to_json()

# convert the object into a dict
printables_post_request_dict = printables_post_request_instance.to_dict()
# create an instance of PrintablesPostRequest from a dict
printables_post_request_form_dict = printables_post_request.from_dict(printables_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


