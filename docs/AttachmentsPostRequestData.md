# AttachmentsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Attachments**](Attachments.md) |  | [optional] 

## Example

```python
from openapi_client.models.attachments_post_request_data import AttachmentsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentsPostRequestData from a JSON string
attachments_post_request_data_instance = AttachmentsPostRequestData.from_json(json)
# print the JSON string representation of the object
print AttachmentsPostRequestData.to_json()

# convert the object into a dict
attachments_post_request_data_dict = attachments_post_request_data_instance.to_dict()
# create an instance of AttachmentsPostRequestData from a dict
attachments_post_request_data_form_dict = attachments_post_request_data.from_dict(attachments_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


