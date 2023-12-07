# AdditionalAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Visible name of the attribute | [optional] 
**attr_key** | **str** | Key for the attribute | [optional] 
**attr_value** | **str** | Value of the attribute | [optional] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 

## Example

```python
from openapi_client.models.additional_attributes import AdditionalAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalAttributes from a JSON string
additional_attributes_instance = AdditionalAttributes.from_json(json)
# print the JSON string representation of the object
print AdditionalAttributes.to_json()

# convert the object into a dict
additional_attributes_dict = additional_attributes_instance.to_dict()
# create an instance of AdditionalAttributes from a dict
additional_attributes_form_dict = additional_attributes.from_dict(additional_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


