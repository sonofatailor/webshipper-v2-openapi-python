# MailTemplates


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**default_locale** | **str** |  | [optional] 
**mail_locales** | **str** |  | [optional] 
**images** | **str** |  | [optional] 
**purpose** | **int** |  | [optional] 
**bcc_mail** | **str** |  | [optional] 
**is_prebuilt** | **bool** |  | [optional] 
**overrides** | **str** |  | [optional] 
**defaults** | **str** |  | [optional] 
**hook** | **str** |  | [optional] 
**whitelisted_languages** | **str** |  | [optional] 
**described** | **str** | Encapsulated with new WYSIWYG editor and legacy HTML based templates | [optional] [readonly] 

## Example

```python
from openapi_client.models.mail_templates import MailTemplates

# TODO update the JSON string below
json = "{}"
# create an instance of MailTemplates from a JSON string
mail_templates_instance = MailTemplates.from_json(json)
# print the JSON string representation of the object
print MailTemplates.to_json()

# convert the object into a dict
mail_templates_dict = mail_templates_instance.to_dict()
# create an instance of MailTemplates from a dict
mail_templates_form_dict = mail_templates.from_dict(mail_templates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


