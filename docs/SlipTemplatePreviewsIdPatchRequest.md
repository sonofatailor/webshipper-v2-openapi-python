# SlipTemplatePreviewsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SlipTemplatePreviewsIdGet200ResponseData**](SlipTemplatePreviewsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.slip_template_previews_id_patch_request import SlipTemplatePreviewsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SlipTemplatePreviewsIdPatchRequest from a JSON string
slip_template_previews_id_patch_request_instance = SlipTemplatePreviewsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print SlipTemplatePreviewsIdPatchRequest.to_json()

# convert the object into a dict
slip_template_previews_id_patch_request_dict = slip_template_previews_id_patch_request_instance.to_dict()
# create an instance of SlipTemplatePreviewsIdPatchRequest from a dict
slip_template_previews_id_patch_request_form_dict = slip_template_previews_id_patch_request.from_dict(slip_template_previews_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


