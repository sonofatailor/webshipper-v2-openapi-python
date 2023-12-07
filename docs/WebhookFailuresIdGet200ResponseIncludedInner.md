# WebhookFailuresIdGet200ResponseIncludedInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**data** | [**WebhookFailuresIdGet200ResponseIncludedInnerData**](WebhookFailuresIdGet200ResponseIncludedInnerData.md) |  | [optional] 

## Example

```python
from webshipperv2.models.webhook_failures_id_get200_response_included_inner import WebhookFailuresIdGet200ResponseIncludedInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookFailuresIdGet200ResponseIncludedInner from a JSON string
webhook_failures_id_get200_response_included_inner_instance = WebhookFailuresIdGet200ResponseIncludedInner.from_json(json)
# print the JSON string representation of the object
print WebhookFailuresIdGet200ResponseIncludedInner.to_json()

# convert the object into a dict
webhook_failures_id_get200_response_included_inner_dict = webhook_failures_id_get200_response_included_inner_instance.to_dict()
# create an instance of WebhookFailuresIdGet200ResponseIncludedInner from a dict
webhook_failures_id_get200_response_included_inner_form_dict = webhook_failures_id_get200_response_included_inner.from_dict(webhook_failures_id_get200_response_included_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


