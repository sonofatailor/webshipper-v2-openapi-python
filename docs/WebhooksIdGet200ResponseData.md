# WebhooksIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Webhooks**](Webhooks.md) |  | [optional] 

## Example

```python
from openapi_client.models.webhooks_id_get200_response_data import WebhooksIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksIdGet200ResponseData from a JSON string
webhooks_id_get200_response_data_instance = WebhooksIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print WebhooksIdGet200ResponseData.to_json()

# convert the object into a dict
webhooks_id_get200_response_data_dict = webhooks_id_get200_response_data_instance.to_dict()
# create an instance of WebhooksIdGet200ResponseData from a dict
webhooks_id_get200_response_data_form_dict = webhooks_id_get200_response_data.from_dict(webhooks_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


