# MailTemplatePreviewsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**MailTemplatePreviews**](MailTemplatePreviews.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_template_previews_post_request_data import MailTemplatePreviewsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of MailTemplatePreviewsPostRequestData from a JSON string
mail_template_previews_post_request_data_instance = MailTemplatePreviewsPostRequestData.from_json(json)
# print the JSON string representation of the object
print MailTemplatePreviewsPostRequestData.to_json()

# convert the object into a dict
mail_template_previews_post_request_data_dict = mail_template_previews_post_request_data_instance.to_dict()
# create an instance of MailTemplatePreviewsPostRequestData from a dict
mail_template_previews_post_request_data_form_dict = mail_template_previews_post_request_data.from_dict(mail_template_previews_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


