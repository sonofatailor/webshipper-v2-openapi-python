# AdditionalAttributesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**AdditionalAttributes**](AdditionalAttributes.md) |  | [optional] 

## Example

```python
from webshipperv2.models.additional_attributes_post_request_data import AdditionalAttributesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalAttributesPostRequestData from a JSON string
additional_attributes_post_request_data_instance = AdditionalAttributesPostRequestData.from_json(json)
# print the JSON string representation of the object
print AdditionalAttributesPostRequestData.to_json()

# convert the object into a dict
additional_attributes_post_request_data_dict = additional_attributes_post_request_data_instance.to_dict()
# create an instance of AdditionalAttributesPostRequestData from a dict
additional_attributes_post_request_data_form_dict = additional_attributes_post_request_data.from_dict(additional_attributes_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


