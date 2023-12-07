# AdditionalAttributesIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AdditionalAttributesIdGet200ResponseData**](AdditionalAttributesIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**AdditionalAttributesIdGet200ResponseRelationships**](AdditionalAttributesIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.additional_attributes_id_patch_request import AdditionalAttributesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalAttributesIdPatchRequest from a JSON string
additional_attributes_id_patch_request_instance = AdditionalAttributesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print AdditionalAttributesIdPatchRequest.to_json()

# convert the object into a dict
additional_attributes_id_patch_request_dict = additional_attributes_id_patch_request_instance.to_dict()
# create an instance of AdditionalAttributesIdPatchRequest from a dict
additional_attributes_id_patch_request_form_dict = additional_attributes_id_patch_request.from_dict(additional_attributes_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


