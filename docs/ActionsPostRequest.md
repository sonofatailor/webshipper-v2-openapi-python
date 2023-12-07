# ActionsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ActionsPostRequestData**](ActionsPostRequestData.md) |  | [optional] 
**relationships** | [**ActionsIdGet200ResponseRelationships**](ActionsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.actions_post_request import ActionsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsPostRequest from a JSON string
actions_post_request_instance = ActionsPostRequest.from_json(json)
# print the JSON string representation of the object
print ActionsPostRequest.to_json()

# convert the object into a dict
actions_post_request_dict = actions_post_request_instance.to_dict()
# create an instance of ActionsPostRequest from a dict
actions_post_request_form_dict = actions_post_request.from_dict(actions_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


