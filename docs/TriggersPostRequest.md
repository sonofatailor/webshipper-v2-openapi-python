# TriggersPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TriggersPostRequestData**](TriggersPostRequestData.md) |  | [optional] 
**relationships** | [**ActionsIdGet200ResponseRelationships**](ActionsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.triggers_post_request import TriggersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TriggersPostRequest from a JSON string
triggers_post_request_instance = TriggersPostRequest.from_json(json)
# print the JSON string representation of the object
print TriggersPostRequest.to_json()

# convert the object into a dict
triggers_post_request_dict = triggers_post_request_instance.to_dict()
# create an instance of TriggersPostRequest from a dict
triggers_post_request_form_dict = triggers_post_request.from_dict(triggers_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


