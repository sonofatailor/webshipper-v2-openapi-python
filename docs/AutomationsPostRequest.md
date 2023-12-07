# AutomationsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AutomationsPostRequestData**](AutomationsPostRequestData.md) |  | [optional] 
**relationships** | [**AutomationsIdGet200ResponseRelationships**](AutomationsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.automations_post_request import AutomationsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationsPostRequest from a JSON string
automations_post_request_instance = AutomationsPostRequest.from_json(json)
# print the JSON string representation of the object
print AutomationsPostRequest.to_json()

# convert the object into a dict
automations_post_request_dict = automations_post_request_instance.to_dict()
# create an instance of AutomationsPostRequest from a dict
automations_post_request_form_dict = automations_post_request.from_dict(automations_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


