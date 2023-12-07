# SlipTemplatesIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SlipTemplatesIdGet200ResponseData**](SlipTemplatesIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.slip_templates_id_patch_request import SlipTemplatesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SlipTemplatesIdPatchRequest from a JSON string
slip_templates_id_patch_request_instance = SlipTemplatesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print SlipTemplatesIdPatchRequest.to_json()

# convert the object into a dict
slip_templates_id_patch_request_dict = slip_templates_id_patch_request_instance.to_dict()
# create an instance of SlipTemplatesIdPatchRequest from a dict
slip_templates_id_patch_request_form_dict = slip_templates_id_patch_request.from_dict(slip_templates_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


