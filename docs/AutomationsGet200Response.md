# AutomationsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AutomationsGet200ResponseDataInner]**](AutomationsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.automations_get200_response import AutomationsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationsGet200Response from a JSON string
automations_get200_response_instance = AutomationsGet200Response.from_json(json)
# print the JSON string representation of the object
print AutomationsGet200Response.to_json()

# convert the object into a dict
automations_get200_response_dict = automations_get200_response_instance.to_dict()
# create an instance of AutomationsGet200Response from a dict
automations_get200_response_form_dict = automations_get200_response.from_dict(automations_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


