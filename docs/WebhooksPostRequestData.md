# WebhooksPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Webhooks**](Webhooks.md) |  | [optional] 

## Example

```python
from openapi_client.models.webhooks_post_request_data import WebhooksPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksPostRequestData from a JSON string
webhooks_post_request_data_instance = WebhooksPostRequestData.from_json(json)
# print the JSON string representation of the object
print WebhooksPostRequestData.to_json()

# convert the object into a dict
webhooks_post_request_data_dict = webhooks_post_request_data_instance.to_dict()
# create an instance of WebhooksPostRequestData from a dict
webhooks_post_request_data_form_dict = webhooks_post_request_data.from_dict(webhooks_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


