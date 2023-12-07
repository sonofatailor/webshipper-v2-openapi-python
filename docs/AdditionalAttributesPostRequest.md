# AdditionalAttributesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AdditionalAttributesPostRequestData**](AdditionalAttributesPostRequestData.md) |  | [optional] 
**relationships** | [**AdditionalAttributesIdGet200ResponseRelationships**](AdditionalAttributesIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.additional_attributes_post_request import AdditionalAttributesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalAttributesPostRequest from a JSON string
additional_attributes_post_request_instance = AdditionalAttributesPostRequest.from_json(json)
# print the JSON string representation of the object
print AdditionalAttributesPostRequest.to_json()

# convert the object into a dict
additional_attributes_post_request_dict = additional_attributes_post_request_instance.to_dict()
# create an instance of AdditionalAttributesPostRequest from a dict
additional_attributes_post_request_form_dict = additional_attributes_post_request.from_dict(additional_attributes_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


