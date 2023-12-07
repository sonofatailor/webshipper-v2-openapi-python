# WebhooksIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhooksIdGet200ResponseData**](WebhooksIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.webhooks_id_get200_response import WebhooksIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksIdGet200Response from a JSON string
webhooks_id_get200_response_instance = WebhooksIdGet200Response.from_json(json)
# print the JSON string representation of the object
print WebhooksIdGet200Response.to_json()

# convert the object into a dict
webhooks_id_get200_response_dict = webhooks_id_get200_response_instance.to_dict()
# create an instance of WebhooksIdGet200Response from a dict
webhooks_id_get200_response_form_dict = webhooks_id_get200_response.from_dict(webhooks_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


