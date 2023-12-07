# AutomationsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Automations**](Automations.md) |  | [optional] 

## Example

```python
from openapi_client.models.automations_post_request_data import AutomationsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationsPostRequestData from a JSON string
automations_post_request_data_instance = AutomationsPostRequestData.from_json(json)
# print the JSON string representation of the object
print AutomationsPostRequestData.to_json()

# convert the object into a dict
automations_post_request_data_dict = automations_post_request_data_instance.to_dict()
# create an instance of AutomationsPostRequestData from a dict
automations_post_request_data_form_dict = automations_post_request_data.from_dict(automations_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


