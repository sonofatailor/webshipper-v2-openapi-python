# AttachmentsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Attachments**](Attachments.md) |  | [optional] 

## Example

```python
from openapi_client.models.attachments_id_get200_response_data import AttachmentsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentsIdGet200ResponseData from a JSON string
attachments_id_get200_response_data_instance = AttachmentsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print AttachmentsIdGet200ResponseData.to_json()

# convert the object into a dict
attachments_id_get200_response_data_dict = attachments_id_get200_response_data_instance.to_dict()
# create an instance of AttachmentsIdGet200ResponseData from a dict
attachments_id_get200_response_data_form_dict = attachments_id_get200_response_data.from_dict(attachments_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


