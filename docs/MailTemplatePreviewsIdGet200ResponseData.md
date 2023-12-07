# MailTemplatePreviewsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**MailTemplatePreviews**](MailTemplatePreviews.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_template_previews_id_get200_response_data import MailTemplatePreviewsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MailTemplatePreviewsIdGet200ResponseData from a JSON string
mail_template_previews_id_get200_response_data_instance = MailTemplatePreviewsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print MailTemplatePreviewsIdGet200ResponseData.to_json()

# convert the object into a dict
mail_template_previews_id_get200_response_data_dict = mail_template_previews_id_get200_response_data_instance.to_dict()
# create an instance of MailTemplatePreviewsIdGet200ResponseData from a dict
mail_template_previews_id_get200_response_data_form_dict = mail_template_previews_id_get200_response_data.from_dict(mail_template_previews_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


