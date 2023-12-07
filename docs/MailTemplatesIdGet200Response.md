# MailTemplatesIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MailTemplatesIdGet200ResponseData**](MailTemplatesIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**MailTemplatesIdGet200ResponseRelationships**](MailTemplatesIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[MailTemplatesIdGet200ResponseIncludedInner]**](MailTemplatesIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_templates_id_get200_response import MailTemplatesIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MailTemplatesIdGet200Response from a JSON string
mail_templates_id_get200_response_instance = MailTemplatesIdGet200Response.from_json(json)
# print the JSON string representation of the object
print MailTemplatesIdGet200Response.to_json()

# convert the object into a dict
mail_templates_id_get200_response_dict = mail_templates_id_get200_response_instance.to_dict()
# create an instance of MailTemplatesIdGet200Response from a dict
mail_templates_id_get200_response_form_dict = mail_templates_id_get200_response.from_dict(mail_templates_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


