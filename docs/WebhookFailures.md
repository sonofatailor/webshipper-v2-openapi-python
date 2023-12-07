# WebhookFailures


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_id** | **int** | The id of the record the webhook failed to send | [optional] [readonly] 
**message** | **str** | Title of the failure | [optional] [readonly] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 

## Example

```python
from openapi_client.models.webhook_failures import WebhookFailures

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookFailures from a JSON string
webhook_failures_instance = WebhookFailures.from_json(json)
# print the JSON string representation of the object
print WebhookFailures.to_json()

# convert the object into a dict
webhook_failures_dict = webhook_failures_instance.to_dict()
# create an instance of WebhookFailures from a dict
webhook_failures_form_dict = webhook_failures.from_dict(webhook_failures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


