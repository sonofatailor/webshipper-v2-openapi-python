# MailTemplatesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**MailTemplates**](MailTemplates.md) |  | [optional] 

## Example

```python
from webshipperv2.models.mail_templates_post_request_data import MailTemplatesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of MailTemplatesPostRequestData from a JSON string
mail_templates_post_request_data_instance = MailTemplatesPostRequestData.from_json(json)
# print the JSON string representation of the object
print MailTemplatesPostRequestData.to_json()

# convert the object into a dict
mail_templates_post_request_data_dict = mail_templates_post_request_data_instance.to_dict()
# create an instance of MailTemplatesPostRequestData from a dict
mail_templates_post_request_data_form_dict = mail_templates_post_request_data.from_dict(mail_templates_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


