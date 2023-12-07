# MailTemplatesIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MailTemplatesIdGet200ResponseData**](MailTemplatesIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**MailTemplatesIdGet200ResponseRelationships**](MailTemplatesIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.mail_templates_id_patch_request import MailTemplatesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MailTemplatesIdPatchRequest from a JSON string
mail_templates_id_patch_request_instance = MailTemplatesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print MailTemplatesIdPatchRequest.to_json()

# convert the object into a dict
mail_templates_id_patch_request_dict = mail_templates_id_patch_request_instance.to_dict()
# create an instance of MailTemplatesIdPatchRequest from a dict
mail_templates_id_patch_request_form_dict = mail_templates_id_patch_request.from_dict(mail_templates_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


