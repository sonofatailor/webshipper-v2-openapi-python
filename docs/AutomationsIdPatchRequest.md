# AutomationsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AutomationsIdGet200ResponseData**](AutomationsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**AutomationsIdGet200ResponseRelationships**](AutomationsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.automations_id_patch_request import AutomationsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationsIdPatchRequest from a JSON string
automations_id_patch_request_instance = AutomationsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print AutomationsIdPatchRequest.to_json()

# convert the object into a dict
automations_id_patch_request_dict = automations_id_patch_request_instance.to_dict()
# create an instance of AutomationsIdPatchRequest from a dict
automations_id_patch_request_form_dict = automations_id_patch_request.from_dict(automations_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


