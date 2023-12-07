# WebhooksIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhooksIdGet200ResponseData**](WebhooksIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.webhooks_id_patch_request import WebhooksIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksIdPatchRequest from a JSON string
webhooks_id_patch_request_instance = WebhooksIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print WebhooksIdPatchRequest.to_json()

# convert the object into a dict
webhooks_id_patch_request_dict = webhooks_id_patch_request_instance.to_dict()
# create an instance of WebhooksIdPatchRequest from a dict
webhooks_id_patch_request_form_dict = webhooks_id_patch_request.from_dict(webhooks_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


