# MailTemplatePreviewsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MailTemplatePreviewsGet200ResponseDataInner]**](MailTemplatePreviewsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_template_previews_get200_response import MailTemplatePreviewsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MailTemplatePreviewsGet200Response from a JSON string
mail_template_previews_get200_response_instance = MailTemplatePreviewsGet200Response.from_json(json)
# print the JSON string representation of the object
print MailTemplatePreviewsGet200Response.to_json()

# convert the object into a dict
mail_template_previews_get200_response_dict = mail_template_previews_get200_response_instance.to_dict()
# create an instance of MailTemplatePreviewsGet200Response from a dict
mail_template_previews_get200_response_form_dict = mail_template_previews_get200_response.from_dict(mail_template_previews_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


