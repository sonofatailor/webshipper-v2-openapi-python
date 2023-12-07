# WebhookFailuresIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhookFailuresIdGet200ResponseData**](WebhookFailuresIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**WebhookFailuresIdGet200ResponseRelationships**](WebhookFailuresIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[WebhookFailuresIdGet200ResponseIncludedInner]**](WebhookFailuresIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.webhook_failures_id_get200_response import WebhookFailuresIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookFailuresIdGet200Response from a JSON string
webhook_failures_id_get200_response_instance = WebhookFailuresIdGet200Response.from_json(json)
# print the JSON string representation of the object
print WebhookFailuresIdGet200Response.to_json()

# convert the object into a dict
webhook_failures_id_get200_response_dict = webhook_failures_id_get200_response_instance.to_dict()
# create an instance of WebhookFailuresIdGet200Response from a dict
webhook_failures_id_get200_response_form_dict = webhook_failures_id_get200_response.from_dict(webhook_failures_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


