# MailTemplatePreviewsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MailTemplatePreviewsPostRequestData**](MailTemplatePreviewsPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.mail_template_previews_post_request import MailTemplatePreviewsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MailTemplatePreviewsPostRequest from a JSON string
mail_template_previews_post_request_instance = MailTemplatePreviewsPostRequest.from_json(json)
# print the JSON string representation of the object
print MailTemplatePreviewsPostRequest.to_json()

# convert the object into a dict
mail_template_previews_post_request_dict = mail_template_previews_post_request_instance.to_dict()
# create an instance of MailTemplatePreviewsPostRequest from a dict
mail_template_previews_post_request_form_dict = mail_template_previews_post_request.from_dict(mail_template_previews_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


