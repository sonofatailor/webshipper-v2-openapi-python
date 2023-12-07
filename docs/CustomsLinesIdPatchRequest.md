# CustomsLinesIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CustomsLinesIdGet200ResponseData**](CustomsLinesIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.customs_lines_id_patch_request import CustomsLinesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomsLinesIdPatchRequest from a JSON string
customs_lines_id_patch_request_instance = CustomsLinesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print CustomsLinesIdPatchRequest.to_json()

# convert the object into a dict
customs_lines_id_patch_request_dict = customs_lines_id_patch_request_instance.to_dict()
# create an instance of CustomsLinesIdPatchRequest from a dict
customs_lines_id_patch_request_form_dict = customs_lines_id_patch_request.from_dict(customs_lines_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


