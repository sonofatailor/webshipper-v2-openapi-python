# SlipTemplatePreviewsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**SlipTemplatePreviews**](SlipTemplatePreviews.md) |  | [optional] 

## Example

```python
from webshipperv2.models.slip_template_previews_post_request_data import SlipTemplatePreviewsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of SlipTemplatePreviewsPostRequestData from a JSON string
slip_template_previews_post_request_data_instance = SlipTemplatePreviewsPostRequestData.from_json(json)
# print the JSON string representation of the object
print SlipTemplatePreviewsPostRequestData.to_json()

# convert the object into a dict
slip_template_previews_post_request_data_dict = slip_template_previews_post_request_data_instance.to_dict()
# create an instance of SlipTemplatePreviewsPostRequestData from a dict
slip_template_previews_post_request_data_form_dict = slip_template_previews_post_request_data.from_dict(slip_template_previews_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


