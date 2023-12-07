# MailTemplatesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MailTemplatesPostRequestData**](MailTemplatesPostRequestData.md) |  | [optional] 
**relationships** | [**MailTemplatesIdGet200ResponseRelationships**](MailTemplatesIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_templates_post_request import MailTemplatesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MailTemplatesPostRequest from a JSON string
mail_templates_post_request_instance = MailTemplatesPostRequest.from_json(json)
# print the JSON string representation of the object
print MailTemplatesPostRequest.to_json()

# convert the object into a dict
mail_templates_post_request_dict = mail_templates_post_request_instance.to_dict()
# create an instance of MailTemplatesPostRequest from a dict
mail_templates_post_request_form_dict = mail_templates_post_request.from_dict(mail_templates_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


