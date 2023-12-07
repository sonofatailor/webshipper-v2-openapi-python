# AdditionalAttributesIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AdditionalAttributesIdGet200ResponseData**](AdditionalAttributesIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**AdditionalAttributesIdGet200ResponseRelationships**](AdditionalAttributesIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[AdditionalAttributesIdGet200ResponseIncludedInner]**](AdditionalAttributesIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.additional_attributes_id_get200_response import AdditionalAttributesIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalAttributesIdGet200Response from a JSON string
additional_attributes_id_get200_response_instance = AdditionalAttributesIdGet200Response.from_json(json)
# print the JSON string representation of the object
print AdditionalAttributesIdGet200Response.to_json()

# convert the object into a dict
additional_attributes_id_get200_response_dict = additional_attributes_id_get200_response_instance.to_dict()
# create an instance of AdditionalAttributesIdGet200Response from a dict
additional_attributes_id_get200_response_form_dict = additional_attributes_id_get200_response.from_dict(additional_attributes_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


