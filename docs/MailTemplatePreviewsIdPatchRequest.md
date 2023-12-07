# MailTemplatePreviewsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MailTemplatePreviewsIdGet200ResponseData**](MailTemplatePreviewsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.mail_template_previews_id_patch_request import MailTemplatePreviewsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MailTemplatePreviewsIdPatchRequest from a JSON string
mail_template_previews_id_patch_request_instance = MailTemplatePreviewsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print MailTemplatePreviewsIdPatchRequest.to_json()

# convert the object into a dict
mail_template_previews_id_patch_request_dict = mail_template_previews_id_patch_request_instance.to_dict()
# create an instance of MailTemplatePreviewsIdPatchRequest from a dict
mail_template_previews_id_patch_request_form_dict = mail_template_previews_id_patch_request.from_dict(mail_template_previews_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


