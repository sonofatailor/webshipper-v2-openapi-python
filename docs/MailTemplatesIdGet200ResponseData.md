# MailTemplatesIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**MailTemplates**](MailTemplates.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_templates_id_get200_response_data import MailTemplatesIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MailTemplatesIdGet200ResponseData from a JSON string
mail_templates_id_get200_response_data_instance = MailTemplatesIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print MailTemplatesIdGet200ResponseData.to_json()

# convert the object into a dict
mail_templates_id_get200_response_data_dict = mail_templates_id_get200_response_data_instance.to_dict()
# create an instance of MailTemplatesIdGet200ResponseData from a dict
mail_templates_id_get200_response_data_form_dict = mail_templates_id_get200_response_data.from_dict(mail_templates_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


