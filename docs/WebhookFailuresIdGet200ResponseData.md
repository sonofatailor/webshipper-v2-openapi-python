# WebhookFailuresIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**WebhookFailures**](WebhookFailures.md) |  | [optional] 

## Example

```python
from webshipperv2.models.webhook_failures_id_get200_response_data import WebhookFailuresIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookFailuresIdGet200ResponseData from a JSON string
webhook_failures_id_get200_response_data_instance = WebhookFailuresIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print WebhookFailuresIdGet200ResponseData.to_json()

# convert the object into a dict
webhook_failures_id_get200_response_data_dict = webhook_failures_id_get200_response_data_instance.to_dict()
# create an instance of WebhookFailuresIdGet200ResponseData from a dict
webhook_failures_id_get200_response_data_form_dict = webhook_failures_id_get200_response_data.from_dict(webhook_failures_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


