# WebhooksPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhooksPostRequestData**](WebhooksPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.webhooks_post_request import WebhooksPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksPostRequest from a JSON string
webhooks_post_request_instance = WebhooksPostRequest.from_json(json)
# print the JSON string representation of the object
print WebhooksPostRequest.to_json()

# convert the object into a dict
webhooks_post_request_dict = webhooks_post_request_instance.to_dict()
# create an instance of WebhooksPostRequest from a dict
webhooks_post_request_form_dict = webhooks_post_request.from_dict(webhooks_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


