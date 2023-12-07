# MailTemplatePreviews


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mail** | **str** |  | [optional] 
**mail_template** | **str** |  | [optional] 
**mail_locale** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**return_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**brand_id** | **str** |  | [optional] 
**hook** | **str** |  | [optional] 
**overrides** | **str** |  | [optional] 
**lang** | **str** |  | [optional] 
**defaults** | **str** |  | [optional] 
**to** | **str** |  | [optional] 
**whitelisted_languages** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.mail_template_previews import MailTemplatePreviews

# TODO update the JSON string below
json = "{}"
# create an instance of MailTemplatePreviews from a JSON string
mail_template_previews_instance = MailTemplatePreviews.from_json(json)
# print the JSON string representation of the object
print MailTemplatePreviews.to_json()

# convert the object into a dict
mail_template_previews_dict = mail_template_previews_instance.to_dict()
# create an instance of MailTemplatePreviews from a dict
mail_template_previews_form_dict = mail_template_previews.from_dict(mail_template_previews_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


