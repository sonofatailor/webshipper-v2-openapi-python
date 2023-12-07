# WebhookFailuresPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhookFailuresPostRequestData**](WebhookFailuresPostRequestData.md) |  | [optional] 
**relationships** | [**WebhookFailuresIdGet200ResponseRelationships**](WebhookFailuresIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.webhook_failures_post_request import WebhookFailuresPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookFailuresPostRequest from a JSON string
webhook_failures_post_request_instance = WebhookFailuresPostRequest.from_json(json)
# print the JSON string representation of the object
print WebhookFailuresPostRequest.to_json()

# convert the object into a dict
webhook_failures_post_request_dict = webhook_failures_post_request_instance.to_dict()
# create an instance of WebhookFailuresPostRequest from a dict
webhook_failures_post_request_form_dict = webhook_failures_post_request.from_dict(webhook_failures_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


