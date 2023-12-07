# WebhookFailuresPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**WebhookFailures**](WebhookFailures.md) |  | [optional] 

## Example

```python
from webshipperv2.models.webhook_failures_post_request_data import WebhookFailuresPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookFailuresPostRequestData from a JSON string
webhook_failures_post_request_data_instance = WebhookFailuresPostRequestData.from_json(json)
# print the JSON string representation of the object
print WebhookFailuresPostRequestData.to_json()

# convert the object into a dict
webhook_failures_post_request_data_dict = webhook_failures_post_request_data_instance.to_dict()
# create an instance of WebhookFailuresPostRequestData from a dict
webhook_failures_post_request_data_form_dict = webhook_failures_post_request_data.from_dict(webhook_failures_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


