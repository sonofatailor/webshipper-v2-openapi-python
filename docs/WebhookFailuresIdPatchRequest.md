# WebhookFailuresIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhookFailuresIdGet200ResponseData**](WebhookFailuresIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**WebhookFailuresIdGet200ResponseRelationships**](WebhookFailuresIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.webhook_failures_id_patch_request import WebhookFailuresIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookFailuresIdPatchRequest from a JSON string
webhook_failures_id_patch_request_instance = WebhookFailuresIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print WebhookFailuresIdPatchRequest.to_json()

# convert the object into a dict
webhook_failures_id_patch_request_dict = webhook_failures_id_patch_request_instance.to_dict()
# create an instance of WebhookFailuresIdPatchRequest from a dict
webhook_failures_id_patch_request_form_dict = webhook_failures_id_patch_request.from_dict(webhook_failures_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


