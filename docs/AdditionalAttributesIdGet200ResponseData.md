# AdditionalAttributesIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**AdditionalAttributes**](AdditionalAttributes.md) |  | [optional] 

## Example

```python
from openapi_client.models.additional_attributes_id_get200_response_data import AdditionalAttributesIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalAttributesIdGet200ResponseData from a JSON string
additional_attributes_id_get200_response_data_instance = AdditionalAttributesIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print AdditionalAttributesIdGet200ResponseData.to_json()

# convert the object into a dict
additional_attributes_id_get200_response_data_dict = additional_attributes_id_get200_response_data_instance.to_dict()
# create an instance of AdditionalAttributesIdGet200ResponseData from a dict
additional_attributes_id_get200_response_data_form_dict = additional_attributes_id_get200_response_data.from_dict(additional_attributes_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


