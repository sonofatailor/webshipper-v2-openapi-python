# SlipTemplatePreviewsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SlipTemplatePreviewsPostRequestData**](SlipTemplatePreviewsPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.slip_template_previews_post_request import SlipTemplatePreviewsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SlipTemplatePreviewsPostRequest from a JSON string
slip_template_previews_post_request_instance = SlipTemplatePreviewsPostRequest.from_json(json)
# print the JSON string representation of the object
print SlipTemplatePreviewsPostRequest.to_json()

# convert the object into a dict
slip_template_previews_post_request_dict = slip_template_previews_post_request_instance.to_dict()
# create an instance of SlipTemplatePreviewsPostRequest from a dict
slip_template_previews_post_request_form_dict = slip_template_previews_post_request.from_dict(slip_template_previews_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


