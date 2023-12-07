# WebhookFailuresGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WebhookFailuresGet200ResponseDataInner]**](WebhookFailuresGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.webhook_failures_get200_response import WebhookFailuresGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookFailuresGet200Response from a JSON string
webhook_failures_get200_response_instance = WebhookFailuresGet200Response.from_json(json)
# print the JSON string representation of the object
print WebhookFailuresGet200Response.to_json()

# convert the object into a dict
webhook_failures_get200_response_dict = webhook_failures_get200_response_instance.to_dict()
# create an instance of WebhookFailuresGet200Response from a dict
webhook_failures_get200_response_form_dict = webhook_failures_get200_response.from_dict(webhook_failures_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


