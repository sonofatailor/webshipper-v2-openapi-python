# MailTemplatePreviewsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MailTemplatePreviewsIdGet200ResponseData**](MailTemplatePreviewsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.mail_template_previews_id_get200_response import MailTemplatePreviewsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MailTemplatePreviewsIdGet200Response from a JSON string
mail_template_previews_id_get200_response_instance = MailTemplatePreviewsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print MailTemplatePreviewsIdGet200Response.to_json()

# convert the object into a dict
mail_template_previews_id_get200_response_dict = mail_template_previews_id_get200_response_instance.to_dict()
# create an instance of MailTemplatePreviewsIdGet200Response from a dict
mail_template_previews_id_get200_response_form_dict = mail_template_previews_id_get200_response.from_dict(mail_template_previews_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


