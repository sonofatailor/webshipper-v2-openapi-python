# WebhookFailuresIdGet200ResponseIncludedInnerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The HTTP endpoint to be called. Webhooks always use POST as the request method. | [optional] 
**topic** | **str** | Which event should trigger the webhooks. Supported topics:     &lt;ul&gt;       &lt;li&gt;&lt;strong&gt;order/created&lt;/strong&gt; triggered when an order is created.&lt;/li&gt;       &lt;li&gt;&lt;strong&gt;order/updated&lt;/strong&gt; triggered when an order is updated.&lt;/li&gt;       &lt;li&gt;&lt;strong&gt;order/deleted&lt;/strong&gt; triggered when an order was deleted.&lt;/li&gt;       &lt;li&gt;&lt;strong&gt;shipment/created&lt;/strong&gt; triggered when a shipment is created.&lt;/li&gt;       &lt;li&gt;&lt;strong&gt;shipment/updated&lt;/strong&gt; triggered when a shipment is updated.&lt;/li&gt;       &lt;li&gt;&lt;strong&gt;shipment/deleted&lt;/strong&gt; triggered when a shipment was deleted.&lt;/li&gt;       &lt;li&gt;&lt;strong&gt;return/created&lt;/strong&gt; triggered when a return is created.&lt;/li&gt;       &lt;li&gt;&lt;strong&gt;return/updated&lt;/strong&gt; triggered when a return is updated.&lt;/li&gt;       &lt;li&gt;&lt;strong&gt;return/deleted&lt;/strong&gt; triggered when a return was deleted.&lt;/li&gt;       &lt;li&gt;&lt;strong&gt;report/created&lt;/strong&gt; triggered when a report is created.&lt;/li&gt;       &lt;li&gt;&lt;strong&gt;report/updated&lt;/strong&gt; triggered when a report is updated.&lt;/li&gt;       &lt;li&gt;&lt;strong&gt;report/deleted&lt;/strong&gt; triggered when a report was deleted.&lt;/li&gt;       &lt;li&gt;&lt;strong&gt;trackingevent/created&lt;/strong&gt; triggered when a tracking event is created.&lt;/li&gt;       &lt;li&gt;&lt;strong&gt;trackingevent/updated&lt;/strong&gt; triggered when a tracking event is updated.&lt;/li&gt;       &lt;li&gt;&lt;strong&gt;trackingevent/deleted&lt;/strong&gt; triggered when a tracking event was deleted.&lt;/li&gt;     &lt;/ul&gt; | [optional] 
**enabled** | **bool** | This is a boolean attribute that specifies whether the webhook is active. | [optional] 
**secret** | **str** | The secret used to sign the HMAC. | [optional] 
**health** | **str** |  | [optional] 
**latest_error** | **str** | The most recent error message. | [optional] 
**condition** | **str** |  | [optional] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**carriers** | **str** |  | [optional] 
**order_channels** | **List[str]** | Array of objects containing keys id and channel_label if condition describes a list of allowed order channels, &lt;code&gt;null&lt;/code&gt; otherwise.  | [optional] [readonly] 

## Example

```python
from webshipperv2.models.webhook_failures_id_get200_response_included_inner_data import WebhookFailuresIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookFailuresIdGet200ResponseIncludedInnerData from a JSON string
webhook_failures_id_get200_response_included_inner_data_instance = WebhookFailuresIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print WebhookFailuresIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
webhook_failures_id_get200_response_included_inner_data_dict = webhook_failures_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of WebhookFailuresIdGet200ResponseIncludedInnerData from a dict
webhook_failures_id_get200_response_included_inner_data_form_dict = webhook_failures_id_get200_response_included_inner_data.from_dict(webhook_failures_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


