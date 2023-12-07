# AttachmentsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AttachmentsGet200ResponseDataInner]**](AttachmentsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.attachments_get200_response import AttachmentsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentsGet200Response from a JSON string
attachments_get200_response_instance = AttachmentsGet200Response.from_json(json)
# print the JSON string representation of the object
print AttachmentsGet200Response.to_json()

# convert the object into a dict
attachments_get200_response_dict = attachments_get200_response_instance.to_dict()
# create an instance of AttachmentsGet200Response from a dict
attachments_get200_response_form_dict = attachments_get200_response.from_dict(attachments_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


