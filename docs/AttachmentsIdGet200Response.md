# AttachmentsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AttachmentsIdGet200ResponseData**](AttachmentsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**AttachmentsIdGet200ResponseRelationships**](AttachmentsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[AttachmentsIdGet200ResponseIncludedInner]**](AttachmentsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.attachments_id_get200_response import AttachmentsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentsIdGet200Response from a JSON string
attachments_id_get200_response_instance = AttachmentsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print AttachmentsIdGet200Response.to_json()

# convert the object into a dict
attachments_id_get200_response_dict = attachments_id_get200_response_instance.to_dict()
# create an instance of AttachmentsIdGet200Response from a dict
attachments_id_get200_response_form_dict = attachments_id_get200_response.from_dict(attachments_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


